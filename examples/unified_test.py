from drift_monitor import detect_drift


# Numerical example
reference_numbers = [
    10, 12, 11, 13, 12, 14, 15
]

current_numbers = [
    50, 55, 52, 60, 58, 62, 65
]


result = detect_drift(
    reference_numbers,
    current_numbers,
    data_type="numerical"
)

print("Numerical Drift:")
print(result)


# Categorical example
reference_categories = [
    "A", "A", "A",
    "B", "B",
    "C", "C"
]

current_categories = [
    "A",
    "B", "B", "B",
    "C", "C", "C"
]


result = detect_drift(
    reference_categories,
    current_categories,
    data_type="categorical"
)

print("\nCategorical Drift:")
print(result)