#!/usr/bin/env python3
"""Summarize an authorized CSV export of Windows authentication events.

Requires Python 3.9 or newer and uses only the Python standard library.
Reconstructed portfolio example based on the historical BeastNet workflow.
This is not an original retained artifact and does not recreate historical
outputs.
"""

import argparse
import csv
from collections import Counter
from pathlib import Path
from typing import Counter as CounterType


EVENT_NAMES = {
    "4624": "Successful logon",
    "4625": "Failed logon",
    "4740": "Account lockout",
}
REQUIRED_COLUMNS = {"Id", "TimeCreated"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count Windows authentication event IDs in an authorized CSV."
    )
    parser.add_argument("csv_file", type=Path, help="Path to the CSV export")
    return parser.parse_args()


def summarize(csv_file: Path) -> CounterType[str]:
    if not csv_file.is_file():
        raise ValueError(f"Input file does not exist: {csv_file}")

    try:
        with csv_file.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise ValueError("Input CSV is empty; it has no header row")

            missing = REQUIRED_COLUMNS - set(reader.fieldnames)
            if missing:
                missing_columns = ", ".join(sorted(missing))
                raise ValueError(f"Input CSV is missing required column(s): {missing_columns}")

            return Counter(
                (row.get("Id") or "").strip()
                for row in reader
                if (row.get("Id") or "").strip()
            )
    except UnicodeDecodeError as error:
        raise ValueError(f"Input file is not valid UTF-8 CSV: {error}") from error
    except (OSError, csv.Error) as error:
        raise RuntimeError(f"Unable to read '{csv_file}': {error}") from error


def main() -> None:
    args = parse_args()
    try:
        counts = summarize(args.csv_file)
    except (RuntimeError, ValueError) as error:
        raise SystemExit(f"Error: {error}") from error

    print(f"Total events: {sum(counts.values())}")
    if not counts:
        print("No event records were found in the CSV.")
    else:
        for event_id, count in sorted(counts.items()):
            label = EVENT_NAMES.get(event_id, "Other")
            print(f"{event_id} ({label}): {count}")
    print(
        "Note: Counts are investigative leads and require contextual validation "
        "of the account, source, host, time, and logon context."
    )


if __name__ == "__main__":
    main()
