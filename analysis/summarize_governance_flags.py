"""
summarize_governance_flags.py

Purpose:
Summarize mock county election-board governance research records.

This script uses fictional sample data only. It does not include real county
findings, internal ACLU work product, legal conclusions, contact details, or
raw outreach notes.
"""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_county_governance_records.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_PATH = OUTPUT_DIR / "governance_review_summary.csv"


def load_records() -> pd.DataFrame:
    """Load the mock county governance records."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Could not find data file: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    required_columns = {
        "county_id",
        "county_name",
        "board_type",
        "enabling_legislation_status",
        "outreach_status",
        "source_status",
        "confidence_level",
        "review_flag",
        "next_step",
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df


def summarize_records(df: pd.DataFrame) -> pd.DataFrame:
    """Create a simple summary by review flag and confidence level."""
    summary = (
        df.groupby(["review_flag", "confidence_level"])
        .size()
        .reset_index(name="county_count")
        .sort_values(["review_flag", "confidence_level"])
    )

    return summary


def main() -> None:
    """Run the mock governance-summary workflow."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    records = load_records()
    summary = summarize_records(records)

    summary.to_csv(OUTPUT_PATH, index=False)

    print("Governance review summary")
    print(summary.to_string(index=False))
    print(f"\nSaved summary to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
