# Drift Monitor

A Python data science library for detecting data drift, data quality issues, and numerical outliers in machine learning datasets.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Tests](https://img.shields.io/badge/Tests-41%20Passing-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📚 Table of Contents

- [Features](#-features)
- [What Problem Does It Solve?](#-what-problem-does-it-solve)
- [Architecture](#️-architecture)
- [Monitoring Workflow](#-monitoring-workflow)
- [Statistical Methods](#-statistical-methods)
- [Installation](#-installation)
- [Basic Usage](#-basic-usage)
- [Configuration](#️-configuration)
- [Output](#-output)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [Example Use Case](#-example-use-case)
- [Important Note](#️-important-note)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Features

- Numerical drift detection
- Categorical drift detection
- Missing-value monitoring
- Duplicate-value monitoring
- Numerical outlier detection
- Configurable monitoring thresholds
- Centralized monitoring pipeline
- Logging
- Input validation
- Automated unit testing
- Integration testing
- 94% overall test coverage

---

## 🧠 What Problem Does It Solve?

Machine learning models are trained using historical data.

But after a model is deployed, production data can change over time.

For example:

### Training Data

Age: 20, 22, 25, 28, 30

### Production Data
Age: 40, 45, 50, 55, 60

The production data is significantly different from the data used to train the model.

This change in data distribution is called **data drift**.

If production data changes significantly, the model may eventually perform differently from how it performed during development.

`Drift Monitor` solves this problem by providing:
- **Early Detection:** Automated warnings before model predictions degrade.
- **Statistical Rigor:** Reliable math-backed distribution metrics (KS-Test, Chi-Square).
- **Pipeline Integration:** Easy integration into existing data validation and retraining workflows.
---
## 🏗️ Architecture

```text
                     Reference Data & Current Data
                                  │
                                  ▼
                          ┌───────────────┐
                          │ Drift Monitor │
                          └───────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
      Numerical Drift     Categorical Drift   Data Quality Checks
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                          Outlier Detection
                                  │
                                  ▼
                          Monitoring Report

```
---
## 🔄 Monitoring Workflow
```text
Reference & Current Datasets
           │
           ▼
    Input Validation
           │
           ▼
 Configuration Validation
           │
           ▼
┌────────────────────────────┐
│      Drift Detection       │
│                            │
│ Numerical   → KS Test      │
│ Categorical → Chi-Square   │
└────────────────────────────┘
           │
           ▼
   Data Quality Checks
           │
           ├── Missing Values
           └── Duplicate Records
           │
           ▼
    Outlier Detection
           │
           ▼
      System Logger
           │
           ▼
    Monitoring Report
```
---

## 📊 Statistical Methods

Drift Monitor uses statistical techniques to compare reference and current datasets.
```
Monitoring Type	         Method
-------------------------------------------------------
Numerical Drift	   ->    Kolmogorov-Smirnov (KS) Test
Categorical Drift  ->    Chi-Square Test
Missing Values	   ->    Missing-value percentage
Duplicates	   ->    Duplicate-row percentage
Outliers	   ->    IQR Method
```

## Numerical Drift

Numerical columns are compared using the Kolmogorov-Smirnov two-sample test.

The KS test compares the distributions of the reference and current data.

A configurable significance threshold is used to determine whether drift is detected.
```text
p-value < threshold
        ↓
   Drift Detected

p-value >= threshold
        ↓
   No Drift Detected
```

## Categorical Drift

Categorical distributions are compared using the Chi-Square statistical test.

This helps identify changes in the distribution of categories between reference and current datasets.

## Outlier Detection

Numerical outliers are detected using the Interquartile Range (IQR) method.
```text
IQR = Q3 - Q1

Lower Bound = Q1 - multiplier × IQR

Upper Bound = Q3 + multiplier × IQR
```

The default multiplier is 1.5.

---

## 📦 Installation

Clone the repository:

```text
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:
```text
cd drift-monitor
```

Install the package:
```text
pip install -e .
```

---

## 🔍 Basic Usage
```text
import pandas as pd

from drift_monitor.monitor import monitor_data

reference = pd.DataFrame({
    "age": [20, 22, 24, 26, 28],
    "city": [
        "Hyderabad",
        "Delhi",
        "Mumbai",
        "Delhi",
        "Hyderabad"
    ]
})

current = pd.DataFrame({
    "age": [40, 42, 44, 46, 48],
    "city": [
        "Bangalore",
        "Chennai",
        "Bangalore",
        "Chennai",
        "Bangalore"
    ]
})

report = monitor_data(
    reference,
    current
)

print(report)
```

The reference dataset represents the data used as the baseline.

The current dataset represents new or production data that needs to be monitored.

---
## ⚙️ Configuration

Drift Monitor provides configurable thresholds using MonitorConfig.

```text
from drift_monitor.config import MonitorConfig

config = MonitorConfig(
    drift_threshold=0.05,
    missing_threshold=0.20,
    duplicate_threshold=0.10,
    outlier_multiplier=1.5
)
```

Pass the configuration to the monitoring pipeline:

```text
report = monitor_data(
    reference,
    current,
    config=config
)
```
## Configuration Parameters

```text
Parameter                  Default        Description
------------------------------------------------------------------
drift_threshold       ->    0.05    ->    Significance threshold used for drift detection
missing_threshold     ->    0.02    ->    Maximum allowed missing-value ratio
duplicate_threshold   ->    0.10    ->    Maximum allowed duplicate-row ratio
outlier_multiplier    ->    1.50    ->    IQR multiplier used for outlier detection
```
---
## 📋 Output

The monitor_data() function returns a dictionary containing four major monitoring sections:
```text
{
    "numerical_drift": {},
    "categorical_drift": {},
    "data_quality": {},
    "outliers": {}
}
```
## Numerical Drift

Contains statistical results for numerical columns, including:

- KS statistic
- p-value
- Drift detection status

Example:
```text
{
    "age": {
        "statistic": 0.8,
        "p_value": 0.01,
        "drift_detected": True
    }
}
```
## Categorical Drift

Contains statistical drift results for categorical columns.

### Data Quality

Contains information about:

- Missing values
- Duplicate records
- Data quality status

### Outliers

Contains information such as:

- Q1
- Q3
- IQR
- Lower bound
- Upper bound
- Outlier count
- Outlier percentage
- Outlier values
---
## 🧪 Testing

The project includes unit tests and integration testing using pytest.

Run all tests:
```text
python -m pytest
```

Run tests with coverage:
```text
python -m pytest --cov=drift_monitor --cov-report=term-missing
```

Current test status:
```text
41 tests passing
94% overall test coverage
```

The test suite covers:

- Numerical drift detection
- Categorical drift detection
- Configuration validation
- Input validation
- Data quality monitoring
- Outlier detection
- Monitoring pipeline
- Integration workflow

---
## 📁 Project Structure
```text
drift-monitor/
│
├── drift_monitor/
│   ├── __init__.py
│   ├── categorical.py
│   ├── config.py
│   ├── detector.py
│   ├── logger.py
│   ├── monitor.py
│   ├── numerical.py
│   ├── outlier.py
│   ├── quality.py
│   ├── report.py
│   └── validation.py
│
├── tests/
│   ├── test_categorical.py
│   ├── test_config.py
│   ├── test_monitor.py
│   ├── test_numerical.py
│   ├── test_outlier.py
│   ├── test_quality.py
│   ├── test_validation.py
│   └── test_integration.py
│
├── examples/
│
├── pyproject.toml
├── README.md
└── LICENSE
```

---
## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- SciPy
- Pytest
- pytest-cov
- Dataclasses
- Python Logging
---
## 🎯 Example Use Case

Suppose a machine learning model was trained using historical customer data.

The model expects features such as:
```text
Age
Income
City
Credit Score
```

After deployment, new customer data starts arriving.

Drift Monitor compares:
```text
Training / Reference Data
            │
            ▼
       Drift Monitor
            ▲
            │
Production / Current Data
```

It can identify:

- Changes in numerical distributions
- Changes in categorical distributions
- Increased missing values
- Increased duplicate records
- Numerical outliers

This allows data scientists and ML engineers to identify potential data problems before they negatively affect the machine learning system.

---
## ⚠️ Important Note

### Data drift does not necessarily mean that model performance has decreased.

Drift indicates that the distribution of incoming data has changed compared with the reference data.

Model performance should be evaluated separately using appropriate model evaluation metrics.

```
Data Drift
    ≠
Model Performance Degradation
```
---
## 🚀 Future Improvements

Planned improvements include:

- GitHub Actions CI/CD
- Docker support
- HTML monitoring reports
- Streamlit monitoring dashboard
- PyPI package distribution
- Additional drift detection methods
- Configurable monitoring schedules
- Historical drift tracking

---
## 📄 License

This project is licensed under the MIT License.

---
## 🐳 Docker

The project can be run inside a Docker container to provide a consistent Python environment.

### Build the Docker image

```bash
docker build -t drift-monitor .
```

### Run the tests inside Docker
```bash
docker run --rm drift-monitor
```

The container automatically runs the project's test suite.

---
## Commit it

After testing:

```bash
git add Dockerfile README.md
```

Then:
```bash
git commit -m "Add Docker support"
```

Then:
```bash
git push origin main
```
---
```text
[![PyPI version](https://img.shields.io/pypi/v/drift-monitor-bhaskar.svg)](https://pypi.org/project/drift-monitor-bhaskar/)
[![Python Versions](https://img.shields.io/pypi/pyversions/drift-monitor-bhaskar.svg)](https://pypi.org/project/drift-monitor-bhaskar/)
```
## Installation

Install the published package from PyPI using `pip`:

```bash
pip install drift-monitor-bhaskar
```

## Usage & Import

Import the package into your Python scripts or Jupyter Notebooks:

```python
import drift_monitor as dm

# Initialize the drift monitor
monitor = dm.DriftMonitor()
```

*Note:* The import package name uses an underscore `drift_monitor` in Python code, whereas the `pip install` package name uses dashes and your suffix `drift-monitor-bhaskar`.)
---
## ‍💻 Author

### Bhaskar Gangapuram

B.Tech Computer Science Engineering

Interested in Data Science, Machine Learning, and MLOps.