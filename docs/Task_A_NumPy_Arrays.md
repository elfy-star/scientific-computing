# Task A (Task 2): NumPy Arrays and Numerical Computation

## Inputs and mathematical operation
The input is one array of 24 hourly temperatures in °C. The operations are the mean, (Σ tᵢ)/24, the minimum and maximum, and the vectorized affine conversion F = 1.8C + 32, applied to every element at once.

## Output and its meaning
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```
The average temperature for the day is 23.12 °C. Assuming the first reading is at midnight, the coolest hour is 03:00 (17.5 °C) and the warmest is 12:00 (29.4 °C), a range of 11.9 °C. The first six Fahrenheit values (about 64 to 66 °F) show the cool early-morning period.

## Changing a parameter
Every reading was raised by 5 °C (`temperatures_c + 5`), as if the day were a warmer one.
```
Mean after +5 C offset: 28.12 C  (min 22.50, max 34.40)
Mean in F: 82.62 F
```
The mean, minimum and maximum each rose by exactly 5 °C, while the range stayed 11.9 °C. Adding a constant shifts all the statistics equally and does not change the spread. In Fahrenheit the shift is 5 × 1.8 = 9 °F, which is why the mean moved from 73.6 °F to 82.6 °F.

## Modified real-world case: greenhouse humidity
**Assumptions:** a sensor records relative humidity (%) every hour for 24 hours; humidity above 65 % encourages fungal disease in the crop, so the farmer wants to know when it is exceeded. **Input data:** 24 hourly humidity values (high at night, low at midday). A boolean mask replaces a loop.

```python
import numpy as np
hum = np.array([62,64,66,67,69,70,68,64,58,52,47,44,42,41,43,46,51,55,58,60,61,62,63,63],float)
print(f"Mean humidity: {hum.mean():.2f} %  min: {hum.min():.0f} %  max: {hum.max():.0f} %")
mask = hum > 65
print("Hours above 65 %:", np.where(mask)[0].tolist(), "count:", int(mask.sum()))
print(f"Mean of those hours: {hum[mask].mean():.2f} %")
```
```
Mean humidity: 57.33 %  min: 41 %  max: 70 %
Hours above 65 %: [2, 3, 4, 5, 6] count: 5
Mean of those hours: 68.00 %
```
**Interpretation:** the average humidity is 57.33 %, but five consecutive hours (indices 2 to 6, about 02:00 to 06:00) are above the 65 % limit, with an average of 68 %. The farmer should schedule ventilation or fans for the early hours rather than all day. A single mean hides this problem, which is why the mask is useful.

*Code: `code/Task_02_numpy_arrays.py` and `code/new_cases/greenhouse_humidity.py`.*
