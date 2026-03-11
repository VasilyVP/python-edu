from scipy.interpolate import UnivariateSpline, interp1d
import numpy as np

# Original data points
xs = np.arange(10)

# Linear interpolation
ys = 2 * xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

# Spline interpolation
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr) 
