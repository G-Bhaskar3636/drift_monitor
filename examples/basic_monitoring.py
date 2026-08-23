import pandas as pd

from drift_monitor.monitor import monitor_data
from drift_monitor.config import MonitorConfig


def main():

    # Reference dataset
    reference = pd.DataFrame({
        "age": [22, 24, 25, 27, 28, 30, 31, 33, 35, 36],
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

    # Current dataset
    current = pd.DataFrame({
        "age": [35, 38, 40, 42, 45, 47, 50, 52, 55, 58],
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

    # Configure monitoring
    config = MonitorConfig(
        drift_threshold=0.05,
        missing_threshold=0.20,
        duplicate_threshold=0.10,
        outlier_multiplier=1.5
    )

    # Run monitoring
    report = monitor_data(
        reference,
        current,
        config=config
    )

    # Display results
    print("\n" + "=" * 50)
    print("DRIFT MONITORING REPORT")
    print("=" * 50)

    print("\nNumerical Drift:")
    for column, result in report["numerical_drift"].items():
        print(
            f"{column}: "
            f"drift_detected={result['drift_detected']}, "
            f"p_value={result['p_value']:.4f}"
        )

    print("\nCategorical Drift:")
    for column, result in report["categorical_drift"].items():
        print(
            f"{column}: "
            f"drift_detected={result['drift_detected']}, "
            f"p_value={result['p_value']:.4f}"
        )

    print("\nOutliers:")
    for column, result in report["outliers"].items():
        print(
            f"{column}: "
            f"{result.get('outlier_count', 0)} outlier(s)"
        )

    print("\nData Quality:")
    print(report["data_quality"])

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()