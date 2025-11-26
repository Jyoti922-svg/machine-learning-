# Instructions for Sharing This Project

## Before Sharing (Creating ZIP)

### Option 1: Include Everything (Recommended for Beginners)

1. **Include the venv folder** - Makes it easier for recipients (but larger file size ~500MB)
   - Just zip the entire project folder
   - Recipients can skip steps 3-5 in installation

### Option 2: Exclude venv (Recommended for Smaller File Size)

1. **Exclude the venv folder** - Smaller ZIP file (~5MB)
   - Recipients will need to create their own venv
   - Use the `.gitignore` file to exclude unnecessary files

**To create ZIP excluding venv:**
- Use 7-Zip, WinRAR, or Windows built-in compression
- Exclude the `venv` folder when creating the archive
- Include all other files

## What to Include in ZIP

✅ **Must Include:**
- All `.py` files (app.py, train_model.py, generate_dataset.py, run.py)
- `requirements.txt`
- `templates/` folder (with index.html)
- `static/` folder (with style.css and main.js)
- `README.md`
- `INSTALLATION.md`
- `SETUP.txt`
- `setup.bat`
- `start.bat`
- `start.ps1`
- `.gitignore`

❓ **Optional (Recommended):**
- `data/metastructure_dataset.csv` (if you want to share the dataset)
- `model/model.pkl` and `model/label_encoder.pkl` (if you want to share trained model)

❌ **Exclude (Can be regenerated):**
- `venv/` folder (unless you want a larger but easier setup)
- `__pycache__/` folders
- `.pyc` files

## Recommended ZIP Structure

```
metastructure-project.zip
│
├─ app.py
├─ train_model.py
├─ generate_dataset.py
├─ run.py
├─ setup.bat
├─ start.bat
├─ start.ps1
├─ requirements.txt
├─ README.md
├─ INSTALLATION.md
├─ SETUP.txt
├─ .gitignore
│
├─ data/
│  └─ metastructure_dataset.csv (optional)
│
├─ model/
│  ├─ model.pkl (optional)
│  └─ label_encoder.pkl (optional)
│
├─ templates/
│  └─ index.html
│
└─ static/
   ├─ style.css
   └─ main.js
```

## Instructions to Give Recipients

Share these files with the recipient:
1. The ZIP file
2. Tell them to read `INSTALLATION.md` or `SETUP.txt` for setup instructions
3. Or tell them to run `setup.bat` (if included) for automatic setup

## Quick Message Template

```
Hi! Here's the ML-Assisted Additive Manufacturing Metastructures project.

SETUP INSTRUCTIONS:
1. Extract the ZIP file
2. Open INSTALLATION.md or SETUP.txt for detailed instructions
3. Or simply run: setup.bat (automatic setup)

REQUIREMENTS:
- Python 3.8 or higher
- Internet connection (for first-time setup)

QUICK START (after setup):
- Run: start.bat
- Open: http://localhost:5000

For any issues, check the troubleshooting section in INSTALLATION.md
```

