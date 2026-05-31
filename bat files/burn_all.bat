@echo off

echo Burning main.py
echo.
uv run mpremote cp main.py :main.py
echo ......................

echo Burning r503u.py
echo.
uv run mpremote cp r503u.py :r503u.py
echo.

pause