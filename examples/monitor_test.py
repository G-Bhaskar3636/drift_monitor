import pandas as pd

from drift_monitor import (
    monitor_data,
    print_report,
    MonitorConfig
)


# -------------------------
# Reference dataset
# -------------------------

reference = pd.DataFrame({
    "age": [
        20, 22, 25, 27, 30,
        32, 35, 38, 40, 42
    ],

    "salary": [
        25000, 28000, 30000, 32000, 35000,
        36000, 38000, 40000, 42000, 45000
    ],

    "city": [
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Hyderabad"
    ]
})


# -------------------------
# Current dataset
# -------------------------

current = pd.DataFrame({
    "age": [
        45, 48, 50, 52, 55,
        58, 60, 62, 65, 70
    ],

    "salary": [
        50000, 52000, 55000, 58000, 60000,
        62000, 65000, 68000, 70000, 500000
    ],

    "city": [
        "Delhi",
        "Delhi",
        "Delhi",
        "Mumbai",
        "Mumbai",
        "Mumbai",
        "Delhi",
        "Delhi",
        "Mumbai",
        "Delhi"
    ]
})


# -------------------------
# Configuration
# -------------------------

config = MonitorConfig(
    drift_threshold=0.01,
    missing_threshold=0.10,
    duplicate_threshold=0.05,
    outlier_multiplier=2.0
)


# -------------------------
# Run monitoring
# -------------------------

report = monitor_data(
    reference,
    current,
    config=config
)


# -------------------------
# Print report
# -------------------------

print_report(report)