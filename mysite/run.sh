#!/bin/bash
# Whispers of Ink - Quick Start Script for Linux/macOS

echo ""
echo "========================================"
echo "   Whispers of Ink - Setup & Run"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ using your package manager"
    exit 1
fi

echo "[1/4] Checking Django installation..."
python3 -m pip show django > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[!] Django not found. Installing..."
    python3 -m pip install django
else
    echo "[OK] Django is installed"
fi

echo ""
echo "[2/4] Running migrations..."
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Migration failed"
    exit 1
fi

echo ""
echo "[3/4] Initializing categories..."
python3 init_data.py
if [ $? -ne 0 ]; then
    echo "ERROR: Data initialization failed"
    exit 1
fi

echo ""
echo "[4/4] Starting development server..."
echo ""
echo "========================================"
echo "   Server running at: http://127.0.0.1:8000"
echo "   Admin panel at: http://127.0.0.1:8000/admin"
echo "   Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python3 manage.py runserver
