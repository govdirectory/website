#!/usr/bin/env python3

import argparse
import glob
import re
from pathlib import Path

import requests


def get_expected_count(file_content):
    match = re.search(r"# expected_result_count: (\d+)", file_content)
    if match:
        return int(match.group(1))
    return None


def execute_sparql_query(endpoint, query):
    headers = {
        "Accept": "application/sparql-results+json",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Govdirectory Data Verification Script/1.0 (govdirectory.org)",
    }
    data = {"query": query}
    response = requests.post(endpoint, headers=headers, data=data)
    response.raise_for_status()
    results = response.json()
    return len(results["results"]["bindings"])


def format_table(headers, rows, col_widths=None):
    if not col_widths:
        col_widths = [
            max(len(str(row[i])) for row in [headers] + rows)
            for i in range(len(headers))
        ]

    separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
    header = "|" + "|".join(f" {h:<{w}} " for h, w in zip(headers, col_widths)) + "|"

    formatted_rows = []
    for row in rows:
        formatted_row = (
            "|"
            + "|".join(f" {str(cell):<{w}} " for cell, w in zip(row, col_widths))
            + "|"
        )
        formatted_rows.append(formatted_row)

    return "\n".join([separator, header, separator] + formatted_rows + [separator])


def get_status_priority(status):
    priority = {"FAIL": 0, "ERROR": 1, "NO COUNT": 2, "PASS": 3}
    return priority.get(status, 4)


def verify_result_counts(path, endpoint):
    paths = (
        [path]
        if path.is_file()
        else glob.iglob(str(path / "**/**/*.rq"), recursive=True)
    )
    paths = list(set(paths))
    results = []
    stats = {"pass": 0, "fail": 0, "error": 0, "no_count": 0}

    headers = ["File", "Status", "Expected", "Actual", "Notes"]

    for filepath in paths:
        with open(filepath, "r") as file:
            content = file.read()
            expected_count = get_expected_count(content)

            if expected_count is None:
                results.append(
                    [filepath, "NO COUNT", "-", "-", "No expected count found"]
                )
                stats["no_count"] += 1
                continue

            try:
                actual_count = execute_sparql_query(endpoint, content)
                if actual_count == expected_count:
                    results.append(
                        [filepath, "PASS", expected_count, actual_count, "-"]
                    )
                    stats["pass"] += 1
                else:
                    if actual_count < expected_count:
                   try:
    if actual_count == expected_count:
        results.append([
            filepath,
            "PASS",
            expected_count,
            actual_count,
            "Counts match"
        ])
        stats["pass"] += 1
    elif actual_count < expected_count:
        results.append([
            filepath,
            "FAIL",
            expected_count,
            actual_count,
            "Too few orgs found"
        ])
        stats["fail"] += 1
    else:
        results.append([
            filepath,
            "FAIL",
            expected_count,
            actual_count,
            "Too many orgs found"
        ])
        stats["fail"] += 1

except requests.RequestException as e:
    results.append([
        filepath,
        "ERROR",
        "-",
        "-",
        str(e)
    ])
    stats["error"] += 1


    # Sort results by status priority and then by filename
    results.sort(key=lambda x: (get_status_priority(x[1]), x[0]))

    print(format_table(headers, results))
    print(f"\nSummary:")
    print(
        f"Total: {len(results)} | Passed: {stats['pass']} | Failed: {stats['fail']} | "
        f"Errors: {stats['error']} | No Count: {stats['no_count']}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify SPARQL query result counts")
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("queries/generators"),
        help="Path to single query file or directory of queries",
    )
    parser.add_argument(
        "--endpoint",
        default="https://query.wikidata.org/sparql",
        help="SPARQL endpoint URL",
    )

    args = parser.parse_args()
    verify_result_counts(args.path, args.endpoint)
