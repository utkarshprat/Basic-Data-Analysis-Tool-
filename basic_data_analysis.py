import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
def load(file):
    data = pd.read_csv(file)
    return data

# Basic Analysis (Mean, Median, Mode)
def analysis(data):
    result = ""
    
    for col in data.columns:
        if data[col].dtype in ['int64', 'float64']:
            # Mean
            mean_val = np.mean(data[col])

            # Median
            sorted_vals = sorted(data[col].dropna())
            n = len(sorted_vals)
            if n % 2 == 1:
                median_val = sorted_vals[n // 2]
            else:
                median_val = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
            
            # Mode
            freq_dict = {}
            for val in data[col]:
                freq_dict[val] = freq_dict.get(val, 0) + 1
            mode_val = max(freq_dict, key=freq_dict.get)

            result += f"{col}:\n  Mean: {mean_val:.2f}\n  Median: {median_val:.2f}\n  Mode: {mode_val}\n\n"
    
    return result

# Visualize Data (Histograms)
def visualize(data):
    for col in data.columns:
        if data[col].dtype in ['int64', 'float64']:
            plt.figure()
            plt.hist(data[col].dropna(), bins=20, color='skyblue', edgecolor='black')
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()
