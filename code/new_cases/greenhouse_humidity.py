"""
Modified real-world case: greenhouse humidity (Task 2, NumPy arrays).

A sensor records relative humidity (%) every hour for 24 hours. Humidity above
65 % encourages fungal disease, so a boolean mask (not a loop) finds the hours
where the limit is exceeded.
"""
import numpy as np

hum = np.array([62,64,66,67,69,70,68,64,58,52,47,44,42,41,43,46,51,55,58,60,61,62,63,63], float)
print(f"Mean humidity: {hum.mean():.2f} %  min: {hum.min():.0f} %  max: {hum.max():.0f} %")
mask = hum > 65
print("Hours above 65 %:", np.where(mask)[0].tolist(), "count:", int(mask.sum()))
print(f"Mean of those hours: {hum[mask].mean():.2f} %")
