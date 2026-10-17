# Implementing Linear Regression from scratch
# Using the Gradient Descent Method
# Decide initial w (weight) and b (bias), and let the model learn from its mistake in every epoch
# Model converges into the optimal prediction 

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
y = np.array([28, 35, 39, 45, 51, 54, 62, 65, 72, 76], dtype=float)

# Initialize the parameters

w = 0.0             # weight or slope
b = 0.0             # bias or y-intercept
alpha = 0.01        # learning Rate
epochs = 10000      # Number of corrections to be made
n = 10              # data-size

for i in range(0, epochs):

    y_pred = w * x + b
    w_derivative = 2 * (np.mean(x * (y_pred - y)))
    b_derivative = 2 * (np.mean(y_pred - y))

    w -= alpha * w_derivative
    b -= alpha * b_derivative


y_final = w * x + b

plt.scatter(x, y, label='Actual Date')
plt.plot(x, y_final, label='Regression Line')

xi = float(input("Enter a value: "))
yi = w * xi + b

print("The Model Predicted: ", yi)






