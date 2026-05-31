@echo off

echo.
cd ..
set /p filename=Enter file name to copy:
echo.

if "%filename%"=="" (
    echo No file name entered.
    pause
    exit /b
)

uv run mpremote cp "%filename%" ":%~nx1"
echo.

pause