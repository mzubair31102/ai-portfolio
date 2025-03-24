@echo on
setlocal enabledelayedexpansion

echo ==========================
echo Step 1: Adding changes to Git
echo ==========================
git add .
if %errorlevel% neq 0 (
    echo ERROR: Failed to add files to Git.
    exit /b %errorlevel%
)
echo Successfully added changes to Git.

:: Step 2: Auto-increment commit version
set "VERSION_FILE=.version"

echo ==========================
echo Step 2: Updating Commit Version
echo ==========================
if not exist %VERSION_FILE% (
    echo v1 > %VERSION_FILE%
    set VERSION=v1
) else (
    for /f "delims=v" %%i in (%VERSION_FILE%) do set /a NEXT_VERSION=%%i+1
    echo v!NEXT_VERSION! > %VERSION_FILE%
    set VERSION=v!NEXT_VERSION!
)
echo Commit version updated to: %VERSION%

:: Commit with the new version number
git commit -m "%VERSION%"
if %errorlevel% neq 0 (
    echo ERROR: Git commit failed.
    exit /b %errorlevel%
)
echo Successfully committed changes.

echo ==========================
echo Step 3: Pushing to GitHub
echo ==========================
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Git push failed.
    exit /b %errorlevel%
)
echo Successfully pushed to GitHub.

:: Step 4: Check if any container is using the image and remove it
set "IMAGE_NAME=ai-portfolio"

echo ==========================
echo Step 4: Stopping & Removing Containers using Image: %IMAGE_NAME%
echo ==========================
for /f %%i in ('docker ps -aq --filter "ancestor=%IMAGE_NAME%"') do (
    echo Stopping container %%i...
    docker stop %%i
    docker rm %%i
    echo Container %%i removed.
)

:: Check if the image exists and remove it
echo ==========================
echo Step 5: Checking & Removing Existing Docker Image
echo ==========================
for /f %%i in ('docker images -q %IMAGE_NAME%') do (
    echo Removing image %IMAGE_NAME%...
    docker rmi -f %%i
    echo Image %IMAGE_NAME% removed.
)

:: Step 6: Build the Docker image
echo ==========================
echo Step 6: Building Docker Image
echo ==========================
docker build -t %IMAGE_NAME% .
if %errorlevel% neq 0 (
    echo ERROR: Docker build failed.
    exit /b %errorlevel%
)
echo Successfully built Docker image: %IMAGE_NAME%

:: Step 7: Run the container with multiple ports
echo ==========================
echo Step 7: Running Docker Container
echo ==========================
docker run -d -p 80:80 -p 5000:5000 -p 5432:5432 %IMAGE_NAME%
if %errorlevel% neq 0 (
    echo ERROR: Docker run failed.
    exit /b %errorlevel%
)
echo Successfully started container from image: %IMAGE_NAME%

echo ==========================
echo Deployment Completed Successfully!
echo ==========================

endlocal
