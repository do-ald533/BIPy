# Building and Running BIPy Executable on Linux

This guide explains how to build and run the BIPy executable on Linux systems.

## Prerequisites

Before building the executable, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package manager)
- Git (to clone the repository, if you haven't already)
- venv module (usually included with Python 3)

## Building the Executable

### Option 1: Using the Build Script

We've provided a convenient build script that handles the PyInstaller configuration automatically:

#### Standard Build

1. Open a terminal in the project root directory
2. Make the build script executable:
   ```bash
   chmod +x build_executable.py
   ```
3. Run the build script:
   ```bash
   python3 build_executable.py
   ```
4. Wait for the build process to complete. This may take a few minutes.
5. The executable will be created in the `dist` directory.

#### Build with Virtual Environment (Recommended)

Building in a virtual environment helps isolate dependencies and ensures a clean build environment:

1. Open a terminal in the project root directory
2. Make the build script executable:
   ```bash
   chmod +x build_executable.py
   ```
3. Run the build script with the virtual environment option:
   ```bash
   python3 build_executable.py --venv
   ```
   This will:
   - Create a virtual environment in `.venv` directory (if it doesn't exist)
   - Install all required dependencies in the virtual environment
   - Build the executable using PyInstaller within the virtual environment

4. If you want to specify a different location for the virtual environment:
   ```bash
   python3 build_executable.py --venv --venv-path /path/to/custom/venv
   ```

5. Wait for the build process to complete. This may take a few minutes.
6. The executable will be created in the `dist` directory.

### Option 2: Manual PyInstaller Command

If you prefer to run PyInstaller directly:

#### Using System Python

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. Run PyInstaller with the following options:
   ```bash
   pyinstaller --name=BIPy \
               --onefile \
               --windowed \
               --icon=src/GUI/assets/icone.ico \
               --add-data=src/GUI/assets:src/GUI/assets \
               --hidden-import=PyQt5.QtCore \
               --hidden-import=PyQt5.QtWidgets \
               --hidden-import=PyQt5.QtGui \
               src/main.py
   ```

#### Using a Virtual Environment (Recommended)

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

3. Install the required dependencies in the virtual environment:
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

4. Run PyInstaller with the following options:
   ```bash
   pyinstaller --name=BIPy \
               --onefile \
               --windowed \
               --icon=src/GUI/assets/icone.ico \
               --add-data=src/GUI/assets:src/GUI/assets \
               --hidden-import=PyQt5.QtCore \
               --hidden-import=PyQt5.QtWidgets \
               --hidden-import=PyQt5.QtGui \
               src/main.py
   ```

5. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

## Running the Executable

After building, you can run the BIPy executable:

1. Navigate to the `dist` directory:
   ```bash
   cd dist
   ```

2. Make the executable file runnable (if it isn't already):
   ```bash
   chmod +x BIPy
   ```

3. Run the executable:
   ```bash
   ./BIPy
   ```

## Troubleshooting

### Missing Libraries

If you encounter errors about missing shared libraries when running the executable, you may need to install additional system dependencies:

```bash
sudo apt-get update
sudo apt-get install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0
```

### Permission Issues

If you get "Permission denied" errors:

```bash
chmod +x dist/BIPy
```

### Path Issues with Assets

If the application can't find its assets, try running it from the project root directory:

```bash
./dist/BIPy
```

## Distribution

To distribute the executable to other Linux systems:

1. Copy the executable file from the `dist` directory
2. Ensure the target system has the necessary system libraries installed (see Troubleshooting section)
3. The executable is self-contained and should run on compatible Linux distributions

## Notes

- The executable was built using PyInstaller, which packages the Python interpreter and all dependencies into a single file
- The build process includes all necessary assets and resources
- The executable should work on most modern Linux distributions with similar architecture
