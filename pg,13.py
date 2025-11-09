"""
Write a program that makes use of a function to display sine,cosine,polynomail and exponential curves.
"""
import numpy as np
import matplotlib.pyplot as plt

def pyPlot():
    x = np.linspace(-10, 10, 200)

    plt.plot(x, np.sin(x), label="Sine")
    plt.plot(x, np.cos(x), label="Cosine")
    plt.plot(x, x**2, label="Polynomial (x^2)")
    plt.plot(x, np.exp(x/5), label="Exponential (e^(x/5))")

    plt.legend()
    plt.title("Function Plots")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.show()

pyPlot()
