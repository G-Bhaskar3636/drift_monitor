import pandas as pd


def detect_outliers(
    df,
    multiplier=1.5
):
    """
    Detect numerical outliers using the IQR method.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    if df.empty:
        raise ValueError(
            "DataFrame cannot be empty."
        )

    if multiplier <= 0:
        raise ValueError(
            "multiplier must be greater than 0."
        )

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns

    report = {}

    for column in numerical_columns:

        data = df[column].dropna()

        if len(data) < 4:
            report[column] = {
                "status": "insufficient_data",
                "outlier_count": 0,
                "outlier_percentage": 0.0
            }

            continue

        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)

        iqr = q3 - q1

        lower_bound = (
            q1 - multiplier * iqr
        )

        upper_bound = (
            q3 + multiplier * iqr
        )

        outliers = data[
            (data < lower_bound)
            | (data > upper_bound)
        ]

        outlier_count = len(outliers)

        outlier_percentage = (
            outlier_count / len(data)
        ) * 100

        report[column] = {
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outlier_count": outlier_count,
            "outlier_percentage": outlier_percentage,
            "outlier_values": outliers.tolist()
        }

    return report