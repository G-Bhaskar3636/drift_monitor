from drift_monitor import detect_drift


# Test 1: Empty reference
try:

    detect_drift(
        [],
        [1, 2, 3],
        data_type="numerical"
    )

except Exception as e:

    print("Test 1:")
    print(e)


# Test 2: Empty current
try:

    detect_drift(
        [1, 2, 3],
        [],
        data_type="numerical"
    )

except Exception as e:

    print("\nTest 2:")
    print(e)


# Test 3: Invalid threshold
try:

    detect_drift(
        [1, 2, 3],
        [4, 5, 6],
        threshold=2
    )

except Exception as e:

    print("\nTest 3:")
    print(e)


# Test 4: Invalid data type
try:

    detect_drift(
        [1, 2, 3],
        [4, 5, 6],
        data_type="text"
    )

except Exception as e:

    print("\nTest 4:")
    print(e)