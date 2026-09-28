@echo off
cd /d "%~dp0"
echo Starte lokalen Entwicklungsserver fuer den Website-Draft...
.\.venv\Scripts\python.exe dev.py
pause
