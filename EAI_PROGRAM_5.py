# IoT Sensor Data Analysis using NumPy
import numpy as np

readings = np.array([23.8, 24.6, 26.1, 27.4, 28.9,
                     29.5, 27.2, 26.0, 25.3, 30.6])

print("Sensor Data:", readings)
print("Mean      :", round(np.mean(readings), 2))
print("Median    :", round(np.median(readings), 2))
print("Minimum   :", np.min(readings))
print("Maximum   :", np.max(readings))
print("Std. Dev. :", round(np.std(readings), 2))

limit = 28.0
above_limit = readings[readings > limit]
print("Values above", limit, ":", above_limit)