"""
Simple Python script to start the Flask application
Run this with: python run.py
"""

import os
import sys
import subprocess

def check_model_files():
    """Check if model files exist"""
    model_path = 'model/model.pkl'
    encoder_path = 'model/label_encoder.pkl'
    
    if not os.path.exists(model_path):
        print("[ERROR] Model file not found!")
        print("Please run: python train_model.py")
        return False
    
    if not os.path.exists(encoder_path):
        print("[ERROR] Label encoder not found!")
        print("Please run: python train_model.py")
        return False
    
    return True

def check_and_setup_venv():
    """Check if venv exists, create and install dependencies if needed"""
    venv_python = 'venv/Scripts/python.exe' if sys.platform == 'win32' else 'venv/bin/python'
    
    if not os.path.exists(venv_python):
        print("Virtual environment not found. Creating...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        
        print("Installing dependencies...")
        subprocess.run([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        subprocess.run([venv_python, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    
    return venv_python

def main():
    print("=" * 40)
    print("ML-Assisted Metastructures Project")
    print("=" * 40)
    print()
    
    # Check model files
    if not check_model_files():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Setup venv if needed
    venv_python = check_and_setup_venv()
    
    print("Starting Flask server...")
    print()
    print("Server will be available at: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print()
    
    # Start Flask server
    try:
        subprocess.run([venv_python, 'app.py'], check=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Failed to start server: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == '__main__':
    main()

