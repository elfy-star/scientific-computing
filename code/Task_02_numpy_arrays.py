"""
BIT 2118 Scientific Computing - Task 2: NumPy Arrays and Numerical Computation

Input : one array of 24 hourly temperatures in degrees C.
Maths : mean = (sum t_i) / 24, minimum, maximum, and the vectorised affine
        conversion F = 1.8 C + 32 applied to every element at once.
Note  : the 24 readings are a simulated day, chosen to match the results
        reported in docs/Task_A_NumPy_Arrays.md.
"""
import numpy as np

# 24 hourly temperatures (deg C), index 0 = midnight
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,   # 00:00 - 05:00
    20.8, 22.7, 24.6, 26.3, 27.9, 29.0,   # 06:00 - 11:00
    29.4, 29.2, 28.9, 27.8, 26.6, 25.3,   # 12:00 - 17:00
    23.9, 22.6, 21.5, 20.6, 19.9, 19.2,   # 18:00 - 23:00
])


def summarise(t):
    """Return mean, min and max of a temperature array."""
    return t.mean(), t.min(), t.max()


def to_fahrenheit(c):
    """Vectorised conversion F = 1.8 C + 32 (no loop needed)."""
    return 1.8 * c + 32


def main():
    mean_c, min_c, max_c = summarise(temperatures_c)
    temperatures_f = to_fahrenheit(temperatures_c)

    print("--- Base case ---")
    print(f"Daily mean temperature: {mean_c:.2f} C")
    print(f"Minimum temperature: {min_c:.2f} C")
    print(f"Maximum temperature: {max_c:.2f} C")
    print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

    # Changing a parameter: every reading raised by 5 C
    warmer = temperatures_c + 5
    m, lo, hi = summarise(warmer)
    print("\n--- Parameter change: +5 C offset ---")
    print(f"Mean after +5 C offset: {m:.2f} C  (min {lo:.2f}, max {hi:.2f})")
    print(f"Mean in F: {to_fahrenheit(m):.2f} F")


if __name__ == "__main__":
    main()
