import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print the tree structure
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)

# Example of making a prediction for a single instance
sample_instance = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example features
predicted_class = clf.predict(sample_instance)
print(f"Predicted class for the sample instance: {iris.target_names[predicted_class][0]}")
