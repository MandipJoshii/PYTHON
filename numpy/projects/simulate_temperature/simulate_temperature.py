import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


np.random.seed(0)

temps = np.random.normal(loc=25, scale = 5, size = 365)

days = np.arange(365)
seasonal_effects = (10 * np.sin(2 * np.pi * days/365))
temps = temps + seasonal_effects 

print("\n",temps, "\n")

date_range = pd.date_range(start = "2025-1-1", periods = 365 , freq = "D")

print(date_range, "\n")

data_frame = pd.DataFrame({
    "DATE":date_range,  
    "TEMPERATURE":temps
    
})
print(data_frame, "\n")

print("AVERAGE TEMPERATURE = ", data_frame["TEMPERATURE"].mean())
print("STANDARD DEVIATION = ", data_frame["TEMPERATURE"].std())
print("MAXIMUM TEMPERATURE = ", data_frame["TEMPERATURE"].max())
print("MAXIMUM TEMPERATURE = ", data_frame["TEMPERATURE"].min())



