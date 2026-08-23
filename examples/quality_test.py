import pandas as pd

from drift_monitor import data_quality_report


df = pd.DataFrame({
    "age": [
        20,
        25,
        30,
        None,
        None
    ],

    "salary": [
        25000,
        30000,
        35000,
        40000,
        40000
    ],

    "city": [
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Delhi",
        "Delhi"
    ]
})


report = data_quality_report(df)

print(report)