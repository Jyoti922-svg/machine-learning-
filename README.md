# Machine-Learning Assisted Design of Additive-Manufacturing Metastructures

> **📦 New to this project?** See [INSTALLATION.md](INSTALLATION.md) for complete setup instructions.

## Project Explanation

### What is this project?

This project is a **Machine Learning (ML) system** that helps engineers and designers choose the best internal structure (metastructure) for 3D-printed objects. When you're designing something to be 3D printed, you need to decide what internal pattern to use - like honeycomb, lattice, or other structures. This ML system makes that decision for you based on the material properties you provide.

### Simple Language Explanation

Imagine you're designing a 3D-printed part. You know:
- How stiff it needs to be (stiffness)
- How dense the material is (density)  
- What material you're using (PLA, ABS, Steel, etc.)

But you don't know which internal structure pattern would work best. This ML system takes those three inputs and recommends the optimal structure pattern (Honeycomb, Lattice, Voronoi, or Gyroid) that will give you the best performance.

### ML Use Case

This is a **classification problem** in machine learning. The model learns from historical data about different combinations of:
- Material properties (stiffness, density)
- Material types (PLA, ABS, Resin, Nylon, Steel)
- The best structure choice for each combination

The model uses a **Random Forest Classifier** - an algorithm that learns patterns from training data and can predict the best structure for new, unseen combinations of inputs.

### Input and Output

**User Input:**
- **Stiffness** (integer, 10-100): Mechanical stiffness value of the material
- **Density** (integer, 5-50): Material density value
- **Material** (dropdown): One of PLA, ABS, Resin, Nylon, or Steel

**Model Output:**
- **Recommended Structure**: One of four structure types:
  - **Honeycomb**: Hexagonal cell pattern, excellent strength-to-weight ratio
  - **Lattice**: Interconnected struts, uniform load distribution
  - **Voronoi**: Natural cellular patterns, good for complex geometries
  - **Gyroid**: Triply periodic surfaces, efficient material distribution
- **Confidence Score**: A percentage (0-100%) indicating how confident the model is in its prediction

### How the Recommendation System Works

1. **Training Phase**: The model is trained on a dataset containing 200-300 examples of different material property combinations and their corresponding optimal structures.

2. **Prediction Phase**: 
   - User provides stiffness, density, and material type
   - The material name is converted to a number (label encoding)
   - The model processes these three features
   - The Random Forest algorithm uses learned patterns to predict the best structure
   - The model also calculates confidence based on how similar the input is to training examples

3. **Decision Logic**: The model considers:
   - Higher stiffness + lower density → Often recommends Gyroid or Lattice
   - Lower stiffness + higher density → Often recommends Honeycomb
   - Material type influences the base strength calculations

### Architecture: Dataset → Model → Flask Backend → Frontend Form

```
┌─────────────────┐
│  Dataset (CSV)  │  Contains 200-300 rows of training data
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  train_model.py │  Trains RandomForestClassifier, saves model.pkl
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   model.pkl     │  Trained ML model (saved)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    app.py       │  Flask backend loads model, provides /predict API
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  index.html     │  Frontend form collects user input
│  main.js        │  JavaScript sends POST request to /predict
│  style.css      │  Styling for beautiful UI
└─────────────────┘
```

**Data Flow:**
1. **Dataset Generation**: `generate_dataset.py` creates synthetic training data
2. **Model Training**: `train_model.py` trains the model and saves it
3. **Backend Server**: `app.py` loads the model and serves predictions via REST API
4. **Frontend**: HTML form sends user input to backend, displays prediction results

---

## Quick Start (Easiest Way)

### Option 1: Use the Startup Script (Recommended)

**Windows - Double-click or run:**
```bash
start.bat
```

**Windows PowerShell:**
```powershell
.\start.ps1
```

**Cross-platform Python script:**
```bash
python run.py
```

These scripts will:
- ✅ Check if model files exist
- ✅ Create virtual environment if needed
- ✅ Install dependencies automatically
- ✅ Start the Flask server

### Option 2: Manual Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Generate Dataset

```bash
python generate_dataset.py
```

This will create `data/metastructure_dataset.csv` with 250 rows of training data.

### Step 5: Train the Model

```bash
python train_model.py
```

This will:
- Load the dataset
- Train a RandomForestClassifier
- Save the model to `model/model.pkl`
- Save the label encoder to `model/label_encoder.pkl`
- Display model accuracy and statistics

### Step 6: Run the Flask Server

```bash
python app.py
```

Or use one of the startup scripts:
- `start.bat` (Windows)
- `start.ps1` (PowerShell)
- `python run.py` (Cross-platform)

The server will start on `http://localhost:5000`

### Step 7: Open in Browser

Navigate to: `http://localhost:5000`

You should see the web interface where you can:
1. Enter stiffness (10-100)
2. Enter density (5-50)
3. Select a material
4. Click "Predict Structure"
5. View the recommended structure and confidence score

---

## Project Structure

```
metastructure-project/
│
├─ data/
│  └─ metastructure_dataset.csv          # Training dataset (250 rows)
│
├─ model/
│  ├─ model.pkl                           # Trained RandomForest model
│  └─ label_encoder.pkl                   # Material label encoder
│
├─ templates/
│  └─ index.html                          # Frontend HTML form
│
├─ static/
│  ├─ style.css                           # Styling for the UI
│  └─ main.js                             # JavaScript for API calls
│
├─ app.py                                 # Flask backend server
├─ train_model.py                         # Model training script
├─ generate_dataset.py                    # Dataset generation script
├─ run.py                                 # Python startup script (cross-platform)
├─ start.bat                              # Windows batch startup script
├─ start.ps1                              # PowerShell startup script
├─ requirements.txt                       # Python dependencies
└─ README.md                              # This file
```

---

## API Endpoints

### GET `/`
Renders the main HTML page with the prediction form.

### POST `/predict`
Accepts JSON payload:
```json
{
  "stiffness": 50,
  "density": 20,
  "material": "PLA"
}
```

Returns JSON response:
```json
{
  "recommended_structure": "Lattice",
  "confidence": 0.82
}
```

---

## Model Details

- **Algorithm**: RandomForestClassifier
- **Features**: stiffness, density, material (encoded)
- **Target**: recommended_structure (Honeycomb, Lattice, Voronoi, Gyroid)
- **Training Data**: 250 samples
- **Test Split**: 80% train, 20% test
- **Expected Accuracy**: ~85-95% (depending on data distribution)

---

## Troubleshooting

### Model files not found
If you see "Model files not found" error:
1. Make sure you've run `python generate_dataset.py` first
2. Then run `python train_model.py` to create the model files

### Port already in use
If port 5000 is already in use, modify `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to use a different port (e.g., `port=5001`)

### Import errors
Make sure your virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- Add more structure types
- Include additional material properties
- Visualize structure patterns
- Export predictions to CAD files
- Add model retraining interface
- Include confidence intervals
- Add batch prediction capability

---

## License

This project is for educational and research purposes.

---

## Contact

For questions or issues, please refer to the project documentation or create an issue in the repository.

