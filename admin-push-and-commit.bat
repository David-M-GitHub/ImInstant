@echo off

REM Add all changes to staging
git add .

REM Ask for a commit message
set /p commitMessage=Enter commit message: 

REM Commit the changes with the provided message
git commit -m "%commitMessage%"

REM Push the changes to the remote repository
git push origin main

REM Pause the script to see the output
pause