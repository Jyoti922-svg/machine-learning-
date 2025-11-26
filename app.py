"""
Flask Backend Server for Additive Manufacturing Metastructures Prediction
"""

from flask import Flask, render_template, request, jsonify
import pickle
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and label encoder
model_path = 'model/model.pkl'
encoder_path = 'model/label_encoder.pkl'

if not os.path.exists(model_path) or not os.path.exists(encoder_path):
    raise FileNotFoundError(
        "Model files not found! Please run 'python train_model.py' first."
    )

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(encoder_path, 'rb') as f:
    label_encoder = pickle.load(f)

# Define valid materials
VALID_MATERIALS = ['PLA', 'ABS', 'Resin', 'Nylon', 'Steel']

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict recommended structure based on input parameters"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        stiffness = data.get('stiffness')
        density = data.get('density')
        material = data.get('material')
        
        # Validate inputs
        if stiffness is None or density is None or material is None:
            return jsonify({'error': 'Missing required fields: stiffness, density, material'}), 400
        
        # Validate ranges
        if not isinstance(stiffness, (int, float)) or stiffness < 10 or stiffness > 100:
            return jsonify({'error': 'Stiffness must be between 10 and 100'}), 400
        
        if not isinstance(density, (int, float)) or density < 5 or density > 50:
            return jsonify({'error': 'Density must be between 5 and 50'}), 400
        
        if material not in VALID_MATERIALS:
            return jsonify({
                'error': f'Material must be one of: {", ".join(VALID_MATERIALS)}'
            }), 400
        
        # Encode material
        material_encoded = label_encoder.transform([material])[0]
        
        # Prepare feature DataFrame with proper column names (to match training data)
        features = pd.DataFrame({
            'stiffness': [stiffness],
            'density': [density],
            'material_encoded': [material_encoded]
        })
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get prediction probabilities for con
        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities))
        
        
        return jsonify({
            'recommended_structure': prediction,
            'confidence': round(confidence, 2)
        })
    
    except ValueError as e:
        return jsonify({'error': f'Invalid material: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Make sure you have trained the model first by running: python train_model.py")
    app.run(debug=True, host='0.0.0.0', port=5000)

