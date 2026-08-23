from drift_monitor.numerical import numerical_drift
import numpy as np


reference = [
    10,
    12,
    np.nan,
    13,
    15
]

current = [
    10,
    11,
    14,
    np.nan,
    16
]


result = numerical_drift(
    reference,
    current
)

print(result)