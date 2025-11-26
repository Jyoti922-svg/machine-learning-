# PowerShell script to start the Flask application
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ML-Assisted Metastructures Project" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if model files exist
if (-not (Test-Path "model\model.pkl")) {
    Write-Host "[ERROR] Model files not found!" -ForegroundColor Red
    Write-Host "Please run: python train_model.py" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

if (-not (Test-Path "model\label_encoder.pkl")) {
    Write-Host "[ERROR] Label encoder not found!" -ForegroundColor Red
    Write-Host "Please run: python train_model.py" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if venv exists, if not create it
if (-not (Test-Path "venv\Scripts\python.exe")) {
    Write-Host "Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    & "venv\Scripts\python.exe" -m pip install --upgrade pip
    & "venv\Scripts\python.exe" -m pip install -r requirements.txt
}

Write-Host "Starting Flask server..." -ForegroundColor Green
Write-Host ""
Write-Host "Server will be available at: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start Flask server using venv Python
& "venv\Scripts\python.exe" app.py

