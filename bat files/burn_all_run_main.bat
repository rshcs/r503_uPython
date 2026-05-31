@echo off

echo Burning main.py
echo.
uv run mpremote cp main.py :main.py
echo ......................

echo Burning r503u.py
echo.
uv run mpremote cp r503u.py :r503u.py
echo.

echo Burning completed, Start running the program...

echo.
uv run mpremote run ../main.py
echo.

pause