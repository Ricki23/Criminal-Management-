# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 1: Data Preprocessing
# No missing values in the Iris dataset, so we skip that part.
# Let's standardize the features using StandardScaler.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Feature Engineering
# Create a new feature: Petal Length-to-Width Ratio
X_train_ratio = X_train_scaled[:, 2] / X_train_scaled[:, 3]
X_test_ratio = X_test_scaled[:, 2] / X_test_scaled[:, 3]

# Step 3: Model Building and Evaluation
# Let's start with Logistic Regression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
y_pred_lr = lr_model.predict(X_test_scaled)

# Evaluate model performance
print("Logistic Regression:")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))
print(confusion_matrix(y_test, y_pred_lr))

# Step 4: Model Interpretation
# Coefficients for Logistic Regression
print("Logistic Regression Coefficients:")
print(lr_model.coef_)

# Step 5: Model Optimization
# Let's fine-tune hyperparameters for Decision Tree
param_grid = {'max_depth': [3, 4, 5, 6], 'min_samples_split': [2, 3, 4]}
dt_model = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(dt_model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)
best_dt_model = grid_search.best_estimator_

# Evaluate optimized model
y_pred_dt = best_dt_model.predict(X_test_scaled)
print("\nOptimized Decision Tree:")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))
print(confusion_matrix(y_test, y_pred_dt))
