from pathlib import Path


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

            print(f"{column:<20} {status}")

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

            print(f"{column:<20} {status}")

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

            print(f"{column:<20} {status}")

    else:
        print("No numerical columns found.")

    print()
    print("=" * 50)


def generate_html_report(
    report,
    output_path="drift_report.html"
):
    """
    Generate an HTML monitoring report.
    """

    numerical = report.get(
        "numerical_drift",
        {}
    )

    categorical = report.get(
        "categorical_drift",
        {}
    )

    quality = report.get(
        "data_quality",
        {}
    )

    outliers = report.get(
        "outliers",
        {}
    )

    # -------------------------
    # Numerical Drift HTML
    # -------------------------

    numerical_rows = ""

    for column, result in numerical.items():

        if result.get("drift_detected"):
            status = "DRIFT"
        else:
            status = "NO DRIFT"

        numerical_rows += f"""
        <tr>
            <td>{column}</td>
            <td>{status}</td>
            <td>{result.get("p_value", "N/A")}</td>
        </tr>
        """

    if not numerical_rows:
        numerical_rows = """
        <tr>
            <td colspan="3">No numerical columns found.</td>
        </tr>
        """

    # -------------------------
    # Categorical Drift HTML
    # -------------------------

    categorical_rows = ""

    for column, result in categorical.items():

        if result.get("drift_detected"):
            status = "DRIFT"
        else:
            status = "NO DRIFT"

        categorical_rows += f"""
        <tr>
            <td>{column}</td>
            <td>{status}</td>
            <td>{result.get("p_value", "N/A")}</td>
        </tr>
        """

    if not categorical_rows:
        categorical_rows = """
        <tr>
            <td colspan="3">No categorical columns found.</td>
        </tr>
        """

    # -------------------------
    # Outlier HTML
    # -------------------------

    outlier_rows = ""

    for column, result in outliers.items():

        count = result.get(
            "outlier_count",
            0
        )

        outlier_rows += f"""
        <tr>
            <td>{column}</td>
            <td>{count}</td>
            <td>{result.get("outlier_percentage", 0):.2f}%</td>
        </tr>
        """

    if not outlier_rows:
        outlier_rows = """
        <tr>
            <td colspan="3">No numerical columns found.</td>
        </tr>
        """

    # -------------------------
    # Overall Status
    # -------------------------

    quality_status = quality.get(
        "status",
        "unknown"
    )

    # -------------------------
    # HTML
    # -------------------------

    html = f"""
<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <title>Drift Monitor Report</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}

        h1 {{
            text-align: center;
        }}

        h2 {{
            margin-top: 35px;
        }}

        .summary {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 25px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}

        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: left;
        }}

        th {{
            background-color: #eeeeee;
        }}

        .drift {{
            font-weight: bold;
        }}

        .no-drift {{
            font-weight: bold;
        }}

    </style>

</head>

<body>

    <h1>Drift Monitor Report</h1>

    <div class="summary">

        <h2>Data Quality Summary</h2>

        <p>
            <strong>Status:</strong>
            {quality_status}
        </p>

        <p>
            <strong>Rows:</strong>
            {quality.get("rows", 0)}
        </p>

        <p>
            <strong>Columns:</strong>
            {quality.get("columns", 0)}
        </p>

        <p>
            <strong>Duplicate Rows:</strong>
            {quality.get("duplicate_rows", 0)}
        </p>

    </div>


    <h2>Numerical Drift</h2>

    <table>

        <tr>
            <th>Column</th>
            <th>Status</th>
            <th>P-Value</th>
        </tr>

        {numerical_rows}

    </table>


    <h2>Categorical Drift</h2>

    <table>

        <tr>
            <th>Column</th>
            <th>Status</th>
            <th>P-Value</th>
        </tr>

        {categorical_rows}

    </table>


    <h2>Outliers</h2>

    <table>

        <tr>
            <th>Column</th>
            <th>Outlier Count</th>
            <th>Percentage</th>
        </tr>

        {outlier_rows}

    </table>

</body>

</html>
"""

    # -------------------------
    # Save HTML
    # -------------------------

    output_path = Path(output_path)

    output_path.write_text(
        html,
        encoding="utf-8"
    )

    return output_path