@echo off
set "directory=.\Project"

for /d %%D in ("%directory%\*") do (
    setlocal enabledelayedexpansion
    set "foldername=%%~nxD"
    if exist "%directory%\!foldername!.zip" del "%directory%\!foldername!.zip"
    cd "%directory%\!foldername!"
    tar -a -c -f "..\!foldername!.zip" *
    endlocal
)

echo All projects in the %directory% directory have been compressed.
