def print_report(report):
    """
    Print a human-readable monitoring report.
    """

    print()
    print("=" * 50)
    print("             DRIFT MONITOR REPORT")
    print("=" * 50)

    # -------------------------
    # Numerical Drift
    # -------------------------

    print("\nNUMERICAL DRIFT")
    print("-" * 50)

    numerical = report.get(
        "numerical_drift",
        {}
    )

    if numerical:

        for column, result in numerical.items():

            if result["drift_detected"]:
                status = "DRIFT 🚨"
            else:
                status = "NO DRIFT ✅"

            print(
                f"{column:<20} {status}"
            )

    else:
        print("No numerical columns found.")

    # -------------------------
    # Categorical Drift
    # -------------------------

    print("\nCATEGORICAL DRIFT")
    print("-" * 50)

    categorical = report.get(
        "categorical_drift",
        {}
    )

    if categorical:

        for column, result in categorical.items():

            if result["drift_detected"]:
                status = "DRIFT 🚨"
            else:
                status = "NO DRIFT ✅"

            print(
                f"{column:<20} {status}"
            )

    else:
        print("No categorical columns found.")

    # -------------------------
    # Data Quality
    # -------------------------

    print("\nDATA QUALITY")
    print("-" * 50)

    quality = report.get(
        "data_quality",
        {}
    )

    if quality:

        overall_status = quality.get(
            "status",
            "unknown"
        )

        print(
            f"{'Overall Status':<20} "
            f"{overall_status.upper()}"
        )

        print(
            f"{'Rows':<20} "
            f"{quality.get('rows', 0)}"
        )

        print(
            f"{'Columns':<20} "
            f"{quality.get('columns', 0)}"
        )

        print(
            f"{'Duplicate Rows':<20} "
            f"{quality.get('duplicate_rows', 0)}"
        )

    # -------------------------
    # Outliers
    # -------------------------

    print("\nOUTLIERS")
    print("-" * 50)

    outliers = report.get(
        "outliers",
        {}
    )

    if outliers:

        for column, result in outliers.items():

            count = result.get(
                "outlier_count",
                0
            )

            if count > 0:
                status = f"{count} 🚨"
            else:
                status = "0 ✅"

            print(
                f"{column:<20} {status}"
            )

    else:
        print("No numerical columns found.")

    print()
    print("=" * 50)