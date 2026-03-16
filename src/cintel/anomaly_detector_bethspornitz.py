"""
anomaly_detector_bethspornitz.py - Static anomaly detection pipeline.

Author: Beth Spornitz
Date: 2026-03-13

Static Data

- Data is taken from an adult clinic dataset.
- The data is static, meaning it does not change over time and is not updated with new records.
- Each row represents a patient visit with two key measurements:
  - age_years: The patient's age in years.
  - height_inches: The patient's height in inches.

Purpose

- Read adult clinic data from a CSV file.
- Detect anomalies in age and height values.
- Add an anomaly_reason column to explain why a record was flagged.
- Log the pipeline process for debugging and transparency.

Paths (relative to repo root)

    INPUT FILE: data/clinic_data_bethspornitz.csv
    OUTPUT FILE: artifacts/anomalies_bethspornitz.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.anomaly_detector_bethspornitz

OBS:
  This file is my modified version of the instructor example.
  I updated the anomaly thresholds for adult clinic data
  and added an anomaly_reason column to the output.
"""

# === DECLARE IMPORTS (packages we will use in this project) ===

# First from the Python standard library (no installation needed)
import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P2", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

# === DECLARE GLOBAL CONSTANTS FOR FILE PATHS ===

DATA_FILE: Final[Path] = DATA_DIR / "clinic_data_bethspornitz.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "anomalies_bethspornitz.csv"


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Log the constants to help with debugging and transparency.
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Call the mkdir() method to ensure it exists
    # The parents=True argument allows it to create any necessary parent directories.
    # The exist_ok=True argument prevents an error if the directory already exists.
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ CSV DATA FILE INTO A POLARS DATAFRAME (TABLE)
    # ----------------------------------------------------
    # Polars is great for tabular data.
    # We will use the polars package to
    # read csv (comma-separated values) files
    # into a two dimensional table (DataFrame).

    # Call the polars library read_csv() method.
    # Pass in (provide) the DATA_FILE path of the CSV file.
    # Name the result "df" as is customary.
    df: pl.DataFrame = pl.read_csv(DATA_FILE)

    # Visually inspect the file in the data/ folder.
    # It has columns named `age_years` and `height_inches`.
    # The DataFrame height attribute returns the number of rows.
    LOG.info(f"Loaded {df.height} patient records")

    # ----------------------------------------------------
    # STEP 2: DEFINE THRESHOLDS AND DETECT ANOMALIES
    # ----------------------------------------------------
    # An anomaly is any value greater than the threshold we set.
    # Domain rule for this example:
    # Anything above  or below these values are suspicious.
    LOG.info("Studying adult clinic ages and heights to find anomalies...")

    MIN_REASONABLE_AGE: Final[float] = 18.0
    MAX_REASONABLE_AGE: Final[float] = 100.0
    MIN_REASONABLE_HEIGHT: Final[float] = 48.0
    MAX_REASONABLE_HEIGHT: Final[float] = 84.0

    LOG.info(f"MIN_REASONABLE_AGE: {MIN_REASONABLE_AGE} in years")
    LOG.info(f"MAX_REASONABLE_AGE: {MAX_REASONABLE_AGE} in years")
    LOG.info(f"MIN_REASONABLE_HEIGHT: {MIN_REASONABLE_HEIGHT} in inches")
    LOG.info(f"MAX_REASONABLE_HEIGHT: {MAX_REASONABLE_HEIGHT} in inches")
    # Create a new DataFrame named anomalies_df that contains
    # only the rows where EITHER
    # the age is TOO HIGH OR TOO LOW
    # the height is TOO HIGH OR TOO LOW
    # A single pipe (|) is the OR operator in polars.
    # We will use greater than or equal to (>=) to find values at or above the threshold.
    anomalies_df: pl.DataFrame = df.with_columns(
        pl.when(
            (pl.col("age_years") < MIN_REASONABLE_AGE)
            & (pl.col("height_inches") < MIN_REASONABLE_HEIGHT)
        )
        .then(pl.lit("age and height anomaly"))
        .when(
            (pl.col("age_years") < MIN_REASONABLE_AGE)
            | (pl.col("age_years") > MAX_REASONABLE_AGE)
        )
        .then(pl.lit("age anomaly"))
        .when(
            (pl.col("height_inches") < MIN_REASONABLE_HEIGHT)
            | (pl.col("height_inches") > MAX_REASONABLE_HEIGHT)
        )
        .then(pl.lit("height anomaly"))
        .otherwise(None)
        .alias("anomaly_reason")
    ).filter(pl.col("anomaly_reason").is_not_null())

    LOG.info(f"Count of anomalies found: {anomalies_df.height}")

    # ----------------------------------------------------
    # STEP 3: SAVE THE OUTPUT ANOMALIES AS EVIDENCE
    # ----------------------------------------------------
    # We call generated files "artifacts".
    # They are important evidence of the work we did and the results we found.
    # We will save the anomalies_df DataFrame as a CSV file in the artifacts/ folder

    # Every Polars DataFrame has a write_csv() method that saves it as a CSV file.
    # Just pass in the full Path to the file you want to create.
    anomalies_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote anomalies file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
