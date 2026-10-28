from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([35, 40, 50, 55, 65, 70])

model = LinearRegression()

model.fit(X, y)

print("Weight: ", model.coef_)
print("Bias: ", model.intercept_)

prediction = model.predict(np.array([[7]]))
print("predicted score: ", prediction[0]) 

plt.scatter(X[:, 0], y)
plt.plot(X[:, 0], model.predict(X))

plt.show()