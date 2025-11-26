@echo off
echo ========================================
echo ML-Assisted Metastructures Project
echo ========================================
echo.

REM Check if model files exist
if not exist "model\model.pkl" (
    echo [ERROR] Model files not found!
    echo Please run: python train_model.py
    pause
    exit /b 1
)

if not exist "model\label_encoder.pkl" (
    echo [ERROR] Label encoder not found!
    echo Please run: python train_model.py
    pause
    exit /b 1
)

REM Check if venv exists, if not create it
if not exist "venv\Scripts\python.exe" (
    echo Virtual environment not found. Creating...
    python -m venv venv
    echo Installing dependencies...
    venv\Scripts\python.exe -m pip install --upgrade pip
    venv\Scripts\python.exe -m pip install -r requirements.txt
)

echo Starting Flask server...
echo.
echo Server will be available at: http://localhost:5000
echo Press CTRL+C to stop the server
echo.

REM Start Flask server using venv Python
venv\Scripts\python.exe app.py

pause

