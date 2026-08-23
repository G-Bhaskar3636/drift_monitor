import pandas as pd

from drift_monitor.outlier import detect_outliers


df = pd.DataFrame({
    "age": [
        20,
        21,
        22,
        23,
        24,
        25,
        100
    ],

    "salary": [
        25000,
        28000,
        30000,
        32000,
        35000,
        38000,
        500000
    ],

    "city": [
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Delhi",
        "Chennai",
        "Hyderabad",
        "Delhi"
    ]
})


report = detect_outliers(df)

for column, result in report.items():

    print(f"\nColumn: {column}")

    print(result)