import pandas as pd

from .detector import detect_drift
from .quality import data_quality_report
from .outlier import detect_outliers
from .logger import get_logger
from .config import MonitorConfig


logger = get_logger()


def monitor_data(
    reference,
    current,
    config=None
):
    """
    Run complete monitoring on reference
    and current datasets.
    """

    # -------------------------
    # Configuration
    # -------------------------

    if config is None:
        config = MonitorConfig()

    config.validate()

    # -------------------------
    # Validate DataFrames
    # -------------------------

    if not isinstance(reference, pd.DataFrame):
        raise TypeError(
            "Reference data must be a pandas DataFrame."
        )

    if not isinstance(current, pd.DataFrame):
        raise TypeError(
            "Current data must be a pandas DataFrame."
        )

    if reference.empty:
        raise ValueError(
            "Reference DataFrame cannot be empty."
        )

    if current.empty:
        raise ValueError(
            "Current DataFrame cannot be empty."
        )

    logger.info("Monitoring started.")

    # -------------------------
    # Store results
    # -------------------------

    report = {
        "numerical_drift": {},
        "categorical_drift": {},
        "data_quality": {},
        "outliers": {}
    }

    # -------------------------
    # Numerical drift
    # -------------------------

    numerical_columns = reference.select_dtypes(
        include="number"
    ).columns

    for column in numerical_columns:

        if column not in current.columns:
            continue

        result = detect_drift(
            reference[column].dropna(),
            current[column].dropna(),
            data_type="numerical",
            threshold=config.drift_threshold
        )

        report["numerical_drift"][column] = result

        if result["drift_detected"]:

            logger.warning(
                f"Numerical drift detected "
                f"in column: {column}"
            )

        else:

            logger.info(
                f"No numerical drift detected "
                f"in column: {column}"
            )

    # -------------------------
    # Categorical drift
    # -------------------------

    categorical_columns = reference.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        if column not in current.columns:
            continue

        result = detect_drift(
            reference[column].dropna(),
            current[column].dropna(),
            data_type="categorical",
            threshold=config.drift_threshold
        )

        report["categorical_drift"][column] = result

        if result["drift_detected"]:

            logger.warning(
                f"Categorical drift detected "
                f"in column: {column}"
            )

        else:

            logger.info(
                f"No categorical drift detected "
                f"in column: {column}"
            )

    # -------------------------
    # Data quality
    # -------------------------

    report["data_quality"] = (
        data_quality_report(
            current,
            missing_threshold=config.missing_threshold,
            duplicate_threshold=config.duplicate_threshold
        )
    )

    # -------------------------
    # Outliers
    # -------------------------

    report["outliers"] = (
        detect_outliers(
            current,
            multiplier=config.outlier_multiplier
        )
    )

    for column, result in report["outliers"].items():

        count = result.get(
            "outlier_count",
            0
        )

        if count > 0:

            logger.warning(
                f"{count} outlier(s) detected "
                f"in column: {column}"
            )

    logger.info("Monitoring completed.")

    return report