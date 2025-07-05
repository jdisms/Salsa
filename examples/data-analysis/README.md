# Data Analysis Examples

This directory contains examples for biological data analysis.

## Example Projects

### Statistical Analysis
- Perform t-tests and ANOVA on experimental data
- Calculate correlation coefficients
- Generate statistical reports
- Handle missing data appropriately

### Visualization Tools
- Create publication-ready plots
- Interactive dashboards for data exploration
- Heat maps for gene expression data
- Scatter plots for correlation analysis

### Machine Learning
- Classify biological samples
- Predict protein function
- Cluster gene expression patterns
- Anomaly detection in lab data

## Getting Started

```python
# Example: Basic statistical analysis
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Example: Compare two treatment groups
def compare_treatments(control_data, treatment_data):
    """Compare two treatment groups using t-test"""
    t_stat, p_value = stats.ttest_ind(control_data, treatment_data)
    
    result = {
        'control_mean': np.mean(control_data),
        'treatment_mean': np.mean(treatment_data),
        't_statistic': t_stat,
        'p_value': p_value,
        'significant': p_value < 0.05
    }
    
    return result

# Example usage
control = [23, 25, 22, 24, 26, 21, 23]
treatment = [28, 30, 27, 29, 31, 26, 28]
result = compare_treatments(control, treatment)
print(f"P-value: {result['p_value']:.4f}")
print(f"Significant: {result['significant']}")
```

## Required Libraries
- **Data Analysis**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn, plotly
- **Machine Learning**: scikit-learn, tensorflow
- **Statistical Analysis**: statsmodels, pingouin