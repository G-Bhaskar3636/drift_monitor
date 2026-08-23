import pandas as pd


def data_quality_report(
    df,
    missing_threshold=0.20,
    duplicate_threshold=0.10
):
    """
    Generate a data quality report with
    pass/fail checks.
    """

    # -------------------------
    # Validate input
    # -------------------------

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    if df.empty:
        raise ValueError(
            "DataFrame cannot be empty."
        )

    if not 0 < missing_threshold <= 1:
        raise ValueError(
            "missing_threshold must be between 0 and 1."
        )

    if not 0 <= duplicate_threshold <= 1:
        raise ValueError(
            "duplicate_threshold must be between 0 and 1."
        )

    # -------------------------
    # Basic information
    # -------------------------

    rows = len(df)
    columns = len(df.columns)

    # -------------------------
    # Missing values
    # -------------------------

    missing_counts = (
        df.isnull()
        .sum()
    )

    missing_percentages = (
        df.isnull()
        .mean()
    )

    missing_status = {}

    for column in df.columns:

        percentage = missing_percentages[column]

        if percentage > missing_threshold:
            missing_status[column] = "fail"

        else:
            missing_status[column] = "pass"

    # -------------------------
    # Duplicate rows
    # -------------------------

    duplicate_count = int(
        df.duplicated().sum()
    )

    duplicate_percentage = (
        duplicate_count / rows
    )

    if duplicate_percentage > duplicate_threshold:
        duplicate_status = "fail"
    else:
        duplicate_status = "pass"

    # -------------------------
    # Overall status
    # -------------------------

    if (
        "fail" in missing_status.values()
        or duplicate_status == "fail"
    ):
        overall_status = "fail"

    else:
        overall_status = "pass"

    # -------------------------
    # Return report
    # -------------------------

    return {
        "status": overall_status,

        "rows": rows,

        "columns": columns,

        "missing_values": (
            missing_counts
            .to_dict()
        ),

        "missing_percentage": (
            missing_percentages
            .mul(100)
            .to_dict()
        ),

        "missing_status": missing_status,

        "duplicate_rows": duplicate_count,

        "duplicate_percentage": (
            duplicate_percentage * 100
        ),

        "duplicate_status": duplicate_status,

        "data_types": (
            df.dtypes
            .astype(str)
            .to_dict()
        )
    }