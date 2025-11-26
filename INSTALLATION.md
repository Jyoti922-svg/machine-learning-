# Complete Installation Guide

This guide will help you set up and run the ML-Assisted Additive Manufacturing Metastructures project from scratch.

---

## Prerequisites

Before starting, ensure you have:

1. **Python 3.8 or higher** installed on your system
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Internet connection** (for downloading packages)

---

## Step-by-Step Installation

### Step 1: Extract the Project

1. Extract the ZIP file to a folder (e.g., `D:\Projects\metastructure-project`)
2. Open Command Prompt or PowerShell in that folder

### Step 2: Verify Python Installation

Open Command Prompt/PowerShell and run:
```bash
python --version
```

You should see something like: `Python 3.11.x` or higher

If you get an error, Python is not installed or not in PATH.

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

This creates a virtual environment folder named `venv`.

### Step 4: Activate Virtual Environment

**On Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**On Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt.

### Step 5: Upgrade pip (Optional but Recommended)

```bash
python -m pip install --upgrade pip
```

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- pandas (data processing)
- numpy (numerical computing)
- scikit-learn (machine learning)

Wait for installation to complete (may take a few minutes).

### Step 7: Generate the Dataset

```bash
python generate_dataset.py
```

This creates `data/metastructure_dataset.csv` with 250 rows of training data.

**Expected output:**
```
Dataset generated successfully!
Total rows: 250
...
```

### Step 8: Train the Machine Learning Model

```bash
python train_model.py
```

This will:
- Load the dataset
- Train a RandomForestClassifier
- Save the model to `model/model.pkl`
- Save the label encoder to `model/label_encoder.pkl`
- Display model accuracy (should be around 80-85%)

**Expected output:**
```
Loading dataset...
Training RandomForestClassifier...
Model Accuracy: 0.8200
Model saved to model/model.pkl
Training completed successfully!
```

### Step 9: Start the Flask Server

**Option A: Using the startup script (Easiest)**
```bash
start.bat
```

**Option B: Manual start**
```bash
python app.py
```

**Expected output:**
```
Starting Flask server...
Make sure you have trained the model first by running: python train_model.py
 * Running on http://127.0.0.1:5000
 * Debugger is active!
```

### Step 10: Open in Browser

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. You should see the prediction form

---

## Quick Start (After First Installation)

Once everything is set up, you only need:

```bash
# Activate venv
venv\Scripts\activate

# Start server
python app.py
```

Or simply:
```bash
start.bat
```

---

## Complete Command List (Copy-Paste Ready)

For Windows Command Prompt, copy and paste these commands one by one:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements.txt

# 5. Generate dataset
python generate_dataset.py

# 6. Train model
python train_model.py

# 7. Start server
python app.py
```

---

## Troubleshooting

### Issue: "python is not recognized"
**Solution:** Python is not installed or not in PATH. Reinstall Python and check "Add Python to PATH" during installation.

### Issue: "pip is not recognized"
**Solution:** Use `python -m pip` instead of just `pip`

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure virtual environment is activated (you should see `(venv)` in prompt)

### Issue: "Model files not found"
**Solution:** Run `python train_model.py` first to create the model files

### Issue: Port 5000 already in use
**Solution:** 
1. Close other applications using port 5000, OR
2. Edit `app.py` and change `port=5000` to `port=5001` (or any other port)

### Issue: PowerShell execution policy error
**Solution:** Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Project Structure After Installation

```
metastructure-project/
│
├─ data/
│  └─ metastructure_dataset.csv          ✅ Created by generate_dataset.py
│
├─ model/
│  ├─ model.pkl                           ✅ Created by train_model.py
│  └─ label_encoder.pkl                   ✅ Created by train_model.py
│
├─ venv/                                  ✅ Created by python -m venv venv
│  └─ (virtual environment files)
│
├─ templates/
│  └─ index.html
│
├─ static/
│  ├─ style.css
│  └─ main.js
│
├─ app.py
├─ train_model.py
├─ generate_dataset.py
├─ run.py
├─ start.bat
├─ start.ps1
├─ requirements.txt
├─ README.md
└─ INSTALLATION.md
```

---

## Verification Checklist

After installation, verify everything works:

- [ ] Python is installed (`python --version`)
- [ ] Virtual environment created (`venv` folder exists)
- [ ] Dependencies installed (no import errors)
- [ ] Dataset generated (`data/metastructure_dataset.csv` exists)
- [ ] Model trained (`model/model.pkl` exists)
- [ ] Server starts without errors
- [ ] Website opens at http://localhost:5000
- [ ] Form submission works and shows predictions

---

## System Requirements

- **Operating System:** Windows 7+, macOS 10.12+, or Linux
- **Python:** 3.8 or higher
- **RAM:** Minimum 2GB (4GB recommended)
- **Disk Space:** ~500MB for Python packages and project files
- **Internet:** Required for initial package installation

---

## Need Help?

If you encounter any issues:
1. Check the Troubleshooting section above
2. Ensure all prerequisites are met
3. Verify you're in the correct directory
4. Make sure virtual environment is activated
5. Check that all steps were completed in order

---

## Summary

**First-time setup (one-time):**
1. Extract project
2. `python -m venv venv`
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `python generate_dataset.py`
6. `python train_model.py`
7. `python app.py`

**Daily use:**
1. `start.bat` (or activate venv and run `python app.py`)

That's it! 🚀

