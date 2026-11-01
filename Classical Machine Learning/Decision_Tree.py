
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Loading our Iris Flower Classification Dataset

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = iris.target_names[y]

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:", X.shape)


# Make a train-test dataset split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Decision Tree Model Creation

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)


# Training

model.fit(X_train, y_train)

# Predicting

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)


# Evaluating

print("\n========== MODEL EVALUATION ==========")

print("Training Accuracy:",
      accuracy_score(y_train, y_train_pred))

print("Testing Accuracy:",
      accuracy_score(y_test, y_test_pred))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_test_pred,
        target_names=iris.target_names
    )
)

print("Tree Depth:", model.get_depth())
print("Number of Leaves:", model.get_n_leaves())


# Confusion Matrix

cm = confusion_matrix(y_test, y_test_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot(cmap="Blues")
plt.title("Decision Tree - Confusion Matrix")
plt.show()


# Tree Visualization

plt.figure(figsize=(20, 12))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    fontsize=9
)

plt.title("Decision Tree Classifier")
plt.show()

# Flower Prediction

new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = model.predict(new_flower)

print("\n========== NEW PREDICTION ==========")
print("Predicted Species:", iris.target_names[prediction[0]])
