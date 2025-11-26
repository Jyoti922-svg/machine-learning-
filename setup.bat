@echo off
echo ========================================
echo ML-Assisted Metastructures - Full Setup
echo ========================================
echo.
echo This script will set up the entire project.
echo Press any key to continue or CTRL+C to cancel...
pause >nul
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/6] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment!
    pause
    exit /b 1
)

echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/6] Upgrading pip...
python -m pip install --upgrade pip --quiet

echo [4/6] Installing dependencies (this may take a few minutes)...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)

echo [5/6] Generating dataset...
python generate_dataset.py
if errorlevel 1 (
    echo [ERROR] Failed to generate dataset!
    pause
    exit /b 1
)

echo [6/6] Training the model...
python train_model.py
if errorlevel 1 (
    echo [ERROR] Failed to train model!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To start the server, run:
echo   start.bat
echo.
echo Or manually:
echo   venv\Scripts\activate
echo   python app.py
echo.
pause

