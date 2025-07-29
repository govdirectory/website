#!/usr/bin/env python3

import argparse
import glob
import re
from pathlib import Path

import requests


def execute_sparql_query(endpoint, query):
    headers = {
        "Accept": "application/sparql-results+json",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Govdirectory Data Verification Script/1.0 (govdirectory.org)",
    }
    data = {"query": query}
    response = requests.post(endpoint, headers=headers, data=data)
    response.raise_for_status()
    return response.json()


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


def check_for_missing_labels(path, endpoint):
    paths = (
        [path]
        if path.is_file()
        else glob.iglob(str(path / "**/**/*.rq"), recursive=True)
    )
    paths = list(set(paths))
    print(f"Found {len(paths)} query files to process.")
    missing_labels = []
    stats = {"processed": 0, "errors": 0}

    headers = ["File", "Variable", "QID"]

    for filepath in paths:
        stats["processed"] += 1
        with open(filepath, "r") as file:
            content = file.read()
            paramized_hook = '{{.}}'
            if paramized_hook in content:
                continue

            try:
                results = execute_sparql_query(endpoint, content)
                for result in results["results"]["bindings"]:
                    for var, value in result.items():
                        if var.endswith("Label"):
                            if re.match(r"Q\d+", value["value"]):
                                missing_labels.append([filepath, var, value["value"]])
            except requests.RequestException as e:
                print(f"Error processing {filepath}: {e}")
                stats["errors"] += 1

    if missing_labels:
        print("Missing Labels Found:")
        print(format_table(headers, missing_labels))
    else:
        print("No missing labels found.")

    print(f"\nSummary:")
    print(
        f"Total Files Processed: {stats['processed']} | Request errors: {stats['errors']}"
    )
    if missing_labels:
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for missing labels in SPARQL query results.")
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("queries"),
        help="Path to single query file or directory of queries",
    )
    parser.add_argument(
        "--endpoint",
        default="https://query.wikidata.org/sparql",
        help="SPARQL endpoint URL",
    )

    args = parser.parse_args()
    check_for_missing_labels(args.path, args.endpoint)
