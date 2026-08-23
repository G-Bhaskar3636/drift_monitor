import pandas as pd

from drift_monitor.monitor import monitor_data
from drift_monitor.config import MonitorConfig


def test_complete_monitoring_workflow():

    # Reference dataset
    reference = pd.DataFrame({
        "age": [
            22, 24, 25, 27, 28,
            30, 31, 33, 35, 36
        ],
        "salary": [
            25000, 27000, 28000, 30000, 32000,
            35000, 36000, 38000, 40000, 42000
        ],
        "city": [
            "Hyderabad",
            "Hyderabad",
            "Delhi",
            "Delhi",
            "Mumbai",
            "Mumbai",
            "Hyderabad",
            "Delhi",
            "Mumbai",
            "Hyderabad"
        ]
    })

    # Current production dataset
    current = pd.DataFrame({
        "age": [
            35, 38, 40, 42, 45,
            47, 50, 52, 55, 58
        ],
        "salary": [
            50000, 55000, 60000, 65000, 70000,
            75000, 80000, 85000, 90000, 500000
        ],
        "city": [
            "Bangalore",
            "Bangalore",
            "Bangalore",
            "Bangalore",
            "Chennai",
            "Chennai",
            "Chennai",
            "Bangalore",
            "Chennai",
            "Bangalore"
        ]
    })

    config = MonitorConfig(
        drift_threshold=0.05,
        missing_threshold=0.20,
        duplicate_threshold=0.10,
        outlier_multiplier=1.5
    )

    result = monitor_data(
        reference,
        current,
        config=config
    )

    # Verify complete report
    assert "numerical_drift" in result
    assert "categorical_drift" in result
    assert "data_quality" in result
    assert "outliers" in result

    # Verify numerical monitoring
    assert "age" in result["numerical_drift"]
    assert "salary" in result["numerical_drift"]

    # Verify categorical monitoring
    assert "city" in result["categorical_drift"]

    # Verify outlier monitoring
    assert "salary" in result["outliers"]
    assert result["outliers"]["salary"]["outlier_count"] >= 1