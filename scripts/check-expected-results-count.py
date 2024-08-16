#!/usr/bin/env python3

import glob
import os
import re

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
    response.raise_for_status()  # Raise an exception for HTTP errors
    results = response.json()
    return len(results["results"]["bindings"])


def verify_result_counts(folder_path, endpoint):
    for filename in glob.iglob(folder_path + "**/*.rq", recursive=True):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as file:
            content = file.read()
            expected_count = get_expected_count(content)
            if expected_count is not None:
                try:
                    actual_count = execute_sparql_query(endpoint, content)
                    if actual_count == expected_count:
                        print(
                            f"{filename}: PASS (Expected: {expected_count}, Actual: {actual_count})"
                        )
                    else:
                        print(
                            f"{filename}: FAIL (Expected: {expected_count}, Actual: {actual_count})"
                        )
                except requests.RequestException as e:
                    print(f"{filename}: ERROR - {str(e)}")
            else:
                print(f"{filename}: No expected count found")


if __name__ == "__main__":
    folder_path = "queries/generators"
    endpoint = "https://query.wikidata.org/sparql"
    verify_result_counts(folder_path, endpoint)
