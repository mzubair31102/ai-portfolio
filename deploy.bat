@echo off
setlocal enabledelayedexpansion

:: Step 1: Git Add
git add .

:: Step 2: Auto-increment commit version
set "VERSION_FILE=.version"

if not exist %VERSION_FILE% (
    echo v1 > %VERSION_FILE%
) else (
    for /f "delims=v" %%i in (%VERSION_FILE%) do set /a NEXT_VERSION=%%i+1
    echo v!NEXT_VERSION! > %VERSION_FILE%
)
for /f %%i in (%VERSION_FILE%) do set VERSION=%%i

:: Commit with the new version number
git commit -m "%VERSION%"

:: Step 3: Push to origin main
git push origin main

:: Step 4: Check if any container is using the image and remove it
set "IMAGE_NAME=ai-portfolio"

:: Find containers using the image
for /f %%i in ('docker ps -aq --filter "ancestor=%IMAGE_NAME%"') do (
    echo Stopping and removing container %%i...
    docker stop %%i
    docker rm %%i
)

:: Check if the image exists and remove it
for /f %%i in ('docker images -q %IMAGE_NAME%') do (
    echo Removing existing image %IMAGE_NAME%...
    docker rmi -f %%i
)

:: Step 5: Build the Docker image
docker build -t %IMAGE_NAME% .

:: Step 6: Run the container with multiple ports
docker run -d -p 80:80 -p 5000:5000 -p 5432:5432 %IMAGE_NAME%

endlocal
