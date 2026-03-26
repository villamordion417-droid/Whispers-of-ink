@echo off
REM Whispers of Ink - Quick Start Script for Windows

echo.
echo ========================================
echo   Whispers of Ink - Setup & Run
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Checking Django installation...
python -m pip show django >nul 2>&1
if errorlevel 1 (
    echo [!] Django not found. Installing...
    python -m pip install django
) else (
    echo [OK] Django is installed
)

echo.
echo [2/4] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Migration failed
    pause
    exit /b 1
)

echo.
echo [3/4] Initializing categories...
python init_data.py
if errorlevel 1 (
    echo ERROR: Data initialization failed
    pause
    exit /b 1
)

echo.
echo [4/4] Starting development server...
echo.
echo ========================================
echo   Server running at: http://127.0.0.1:8000
echo   Admin panel at: http://127.0.0.1:8000/admin
echo   Press Ctrl+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause
