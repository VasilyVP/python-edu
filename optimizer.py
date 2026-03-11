from scipy.optimize import minimize
from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np


def eqn(x):
    return x**2 + 10 * x - 5


x = np.linspace(-10, 10, 100)
y = eqn(x)

plt.plot(x, y)
plt.axhline(0, color="red", lw=0.5)
plt.title("Plot of the function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

myroot = root(eqn, 0, method="hybr")

print("Root:", myroot.success)
print("Root value:", myroot.x)

mymin = minimize(eqn, 3, method="BFGS")

print("Minimum:", mymin.success)
print("Minimum value:", mymin.x)
