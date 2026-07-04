@echo off
REM Apply Archi Branding Wrapper
REM
REM Doel: Entoli-merkstyling (opnieuw) toepassen op het door Archi
REM       gegenereerde model.css, na een export vanuit Archi.
REM Usage: apply-archi-branding.bat
REM
REM Vereisten: PowerShell beschikbaar in PATH

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\apply-archi-branding.ps1"
IF ERRORLEVEL 1 (
    echo [ERROR] Toepassen van branding gefaald
    exit /b 1
)

echo [OK] Entoli-branding toegepast
