@echo off

@echo off
echo.
uv run mpremote ls
echo.

echo.
set /p filename=Enter file name to read:
echo.

if "%filename%"=="" (
    echo No file name entered.
    echo.
    pause
    exit /b
)

uv run mpremote cat "%filename%"

echo.
pause