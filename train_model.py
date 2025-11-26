"""
Model Training Script for Additive Manufacturing Metastructures
Trains a RandomForestClassifier to predict recommended structure
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os


os.makedirs('model', exist_ok=True)

# Load dataset
print("Loading dataset...")
df = pd.read_csv('data/metastructure_dataset.csv')

print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())

# Prepare features and target
X = df[['stiffness', 'density', 'material']].copy()
y = df['recommended_structure'].copy()

# Label encode material column
print("\nEncoding material column...")
label_encoder = LabelEncoder()
X['material_encoded'] = label_encoder.fit_transform(X['material'])

# Drop original material column
X = X[['stiffness', 'density', 'material_encoded']]

# Split data
print("\nSplitting data into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# Train RandomForestClassifier
print("\nTraining RandomForestClassifier...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate model
print("\nEvaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model and label encoder
print("\nSaving model and label encoder...")
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("Model saved to model/model.pkl")
print("Label encoder saved to model/label_encoder.pkl")

# Display feature importance
print("\nFeature Importance:")
feature_names = ['stiffness', 'density', 'material_encoded']
importances = model.feature_importances_
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

print("\nTraining completed successfully!")

