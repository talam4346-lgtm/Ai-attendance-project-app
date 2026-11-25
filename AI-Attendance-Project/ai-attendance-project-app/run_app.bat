@echo off
setlocal
cd /d "%~dp0"

set "PYTHON=python"
if exist "..\.venv\Scripts\python.exe" (
	"..\.venv\Scripts\python.exe" -c "import streamlit" >nul 2>&1
	if not errorlevel 1 set "PYTHON=..\.venv\Scripts\python.exe"
)

"%PYTHON%" -m streamlit run app.py --server.headless true --server.port 8501
pause
