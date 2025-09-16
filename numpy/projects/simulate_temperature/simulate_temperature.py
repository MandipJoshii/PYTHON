import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


np.random.seed(0)

temps = np.random.normal(loc=25, scale = 5, size = 365)

days = np.arange(365)
seasonal_effects = (10 * np.sin(2 * np.pi * days/365))
temps = temps + seasonal_effects 

print(temps)


