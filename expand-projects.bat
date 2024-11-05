@echo off
set "directory=.\Project"

for %%Z in ("%directory%\*.zip") do (
    setlocal enabledelayedexpansion
    set "zipfile=%%~nxZ"
    set "foldername=!zipfile:.zip=!"

    if exist "%directory%\!foldername!" rd /s /q "%directory%\!foldername!"
    mkdir "%directory%\!foldername!"
    
    tar -xf "%%Z" -C "%directory%\!foldername!"
    endlocal
)

echo All project files in the %directory% directory have been expanded.
