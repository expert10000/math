@echo off
setlocal
cd /d "%~dp0"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0BUILD_ALL.ps1" %*
set ERR=%ERRORLEVEL%

echo.
if not "%ERR%"=="0" (
  echo BUILD_ALL finished with errors. Exit code: %ERR%
) else (
  echo BUILD_ALL finished successfully.
)

exit /b %ERR%
