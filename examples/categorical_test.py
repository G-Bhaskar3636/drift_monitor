from drift_monitor.categorical import categorical_drift


# -------------------------
# Test 1: Drift
# -------------------------

reference = [
    "A", "A", "A",
    "B", "B",
    "C", "C"
]

current = [
    "A",
    "B", "B", "B",
    "C", "C", "C"
]

result = categorical_drift(
    reference,
    current
)

print("Drift Test:")
print(result)


# -------------------------
# Test 2: No Drift
# -------------------------

reference = [
    "A", "A", "A",
    "B", "B",
    "C", "C"
]

current = [
    "A", "A", "A",
    "B", "B",
    "C", "C"
]

result = categorical_drift(
    reference,
    current
)

print("\nNo Drift Test:")
print(result)