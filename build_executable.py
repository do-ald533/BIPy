#!/usr/bin/env python3
"""
Build script for creating a PyInstaller executable for BIPy
"""
import os
import sys
import subprocess
import argparse
import venv

def create_virtual_env(venv_path):
    """Create a virtual environment at the specified path"""
    print(f"Creating virtual environment at {venv_path}...")
    venv.create(venv_path, with_pip=True)
    return venv_path

def get_venv_python(venv_path):
    """Get the path to the Python executable in the virtual environment"""
    if os.name == 'nt':  # Windows
        return os.path.join(venv_path, 'Scripts', 'python.exe')
    else:  # Linux/Mac
        return os.path.join(venv_path, 'bin', 'python')

def run_in_venv(venv_path, cmd, cwd=None):
    """Run a command in the virtual environment"""
    python_path = get_venv_python(venv_path)
    if isinstance(cmd, list):
        cmd = [python_path] + cmd[1:]
    else:
        cmd = f"{python_path} {cmd}"
    return subprocess.run(cmd, shell=not isinstance(cmd, list), cwd=cwd)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Build BIPy executable')
    parser.add_argument('--venv', action='store_true', help='Use a virtual environment for building')
    parser.add_argument('--venv-path', default='.venv', help='Path to virtual environment (default: .venv)')
    args = parser.parse_args()
    
    # Ensure we're in the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # Setup virtual environment if requested
    if args.venv:
        venv_path = os.path.abspath(args.venv_path)
        if not os.path.exists(venv_path):
            create_virtual_env(venv_path)
        
        # Install dependencies in the virtual environment
        print("Installing required dependencies in virtual environment...")
        run_in_venv(venv_path, [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        run_in_venv(venv_path, [sys.executable, "-m", "pip", "install", "pyinstaller"])
        
        # Define PyInstaller command
        print("Building executable with PyInstaller in virtual environment...")
        pyinstaller_cmd = [
            sys.executable, "-m", "PyInstaller",
            "--name=BIPy",
            "--onefile",
            "--windowed",
            "--icon=src/GUI/assets/icone.ico",
            "--add-data=src/GUI/assets:src/GUI/assets",
            "--hidden-import=PyQt5.QtCore",
            "--hidden-import=PyQt5.QtWidgets",
            "--hidden-import=PyQt5.QtGui",
            "src/main.py"
        ]
        
        # Run PyInstaller in the virtual environment
        result = run_in_venv(venv_path, pyinstaller_cmd)
    else:
        # Install required dependencies in the current Python environment
        print("Installing required dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        
        # Define PyInstaller command with all necessary options
        pyinstaller_cmd = [
            "pyinstaller",
            "--name=BIPy",
            "--onefile",  # Create a single executable file
            "--windowed",  # Don't show console window (for GUI apps)
            "--icon=src/GUI/assets/icone.ico",  # Application icon
            "--add-data=src/GUI/assets:src/GUI/assets",  # Include assets
            "--hidden-import=PyQt5.QtCore",
            "--hidden-import=PyQt5.QtWidgets",
            "--hidden-import=PyQt5.QtGui",
            "src/main.py"  # Main script
        ]
        
        # Run PyInstaller
        print("Building executable with PyInstaller...")
        result = subprocess.run(pyinstaller_cmd)
    
    if result.returncode == 0:
        print("\nBuild successful!")
        print("Executable can be found in the 'dist' directory")
    else:
        print("\nBuild failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
