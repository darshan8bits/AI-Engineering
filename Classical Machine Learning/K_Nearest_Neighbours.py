import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Load the dataset

iris = load_iris()

X = iris.data
y = iris.target

print("Features:", iris.feature_names)
print("Classes:", iris.target_names)
print("Dataset shape:", X.shape)

# Splitting into Training and Testing Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Feature Scaling: Most important part in KNN
# We have used StandardScaler() here, which scales every feature to
# Xnew = (Xold - mean) / (Standard Deviation)
# We have another type of scaling, MinMax Scaling (Converts features in a range from [0, 1])
# Which is Xnew = (Xold - Xmin) / (Xmax - Xmin)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# We did scaler.transform in testing to prevent data leakage

knn = KNeighborsClassifier(
    n_neighbors=5,
    metric="euclidean",
    weights="uniform"
)

knn.fit(X_train, y_train)

# Predictions

y_pred = knn.predict(X_test)

# Model Evaluation

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot(cmap="Blues")
plt.title("KNN Confusion Matrix")
plt.show()

# Predicting an unknown sample

new_sample = [[5.1, 3.5, 1.4, 0.2]]

new_sample_scaled = scaler.transform(new_sample)

prediction = knn.predict(new_sample_scaled)

print("\nPredicted class:", iris.target_names[prediction[0]])
