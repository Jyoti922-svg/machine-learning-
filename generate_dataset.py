"""
Dataset Generator for Additive Manufacturing Metastructures
Generates synthetic dataset with 200-300 rows for training the ML model
"""

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define materials and structures
materials = ['PLA', 'ABS', 'Resin', 'Nylon', 'Steel']
structures = ['Honeycomb', 'Lattice', 'Voronoi', 'Gyroid']

# Generate 250 rows of data
n_samples = 250
data = []

for i in range(n_samples):
    # Generate random values within specified ranges
    stiffness = random.randint(10, 100)
    density = random.randint(5, 50)
    material = random.choice(materials)
    
    # Calculate strength_score based on material properties and structure characteristics
    # Different materials have different base strengths
    material_base_strength = {
        'PLA': 0.6,
        'ABS': 0.7,
        'Resin': 0.75,
        'Nylon': 0.8,
        'Steel': 0.95
    }
    
    # Structure efficiency factors
    structure_efficiency = {
        'Honeycomb': 0.85,
        'Lattice': 0.75,
        'Voronoi': 0.70,
        'Gyroid': 0.80
    }
    
    # Determine recommended structure based on stiffness, density, and material
    # Higher stiffness + lower density -> Lattice or Gyroid
    # Lower stiffness + higher density -> Honeycomb
    # Medium values -> Voronoi
    
    stiffness_ratio = stiffness / 100.0
    density_ratio = density / 50.0
    
    if stiffness_ratio > 0.7 and density_ratio < 0.4:
        recommended_structure = 'Gyroid'
    elif stiffness_ratio > 0.6 and density_ratio < 0.5:
        recommended_structure = 'Lattice'
    elif stiffness_ratio < 0.4 and density_ratio > 0.6:
        recommended_structure = 'Honeycomb'
    elif stiffness_ratio > 0.5:
        recommended_structure = 'Lattice'
    else:
        recommended_structure = 'Voronoi'
    
    # Add some randomness to make it more realistic
    if random.random() < 0.2:
        recommended_structure = random.choice(structures)
    
    # Calculate strength_score
    base_strength = material_base_strength[material]
    efficiency = structure_efficiency[recommended_structure]
    strength_score = base_strength * efficiency * (stiffness / 100.0) * (1 - density / 100.0) + random.uniform(0.1, 0.3)
    strength_score = round(strength_score, 2)
    
    data.append({
        'stiffness': stiffness,
        'density': density,
        'material': material,
        'strength_score': strength_score,
        'recommended_structure': recommended_structure
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/metastructure_dataset.csv', index=False)

print(f"Dataset generated successfully!")
print(f"Total rows: {len(df)}")
print(f"\nDataset preview:")
print(df.head(10))
print(f"\nDataset statistics:")
print(df.describe())
print(f"\nStructure distribution:")
print(df['recommended_structure'].value_counts())
print(f"\nMaterial distribution:")
print(df['material'].value_counts())

