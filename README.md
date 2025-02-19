# LinkedIn Profile Image Downloader

This project downloads your LinkedIn profile image using Selenium with Firefox (via GeckoDriver) running inside a Docker container. The script logs into LinkedIn using your credentials and saves the profile image as `linkedin_profile.jpg` in the project directory.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed and running.
- [Docker Compose](https://docs.docker.com/compose/install/) must be installed.
- A valid LinkedIn account.

## How It Works

- The **Dockerfile** sets up a container with Python, Firefox ESR, and GeckoDriver.
- The Python script (`getter_script.py`) uses Selenium to log into LinkedIn and download your profile image.
- The container mounts your project directory (`.`) to `/app` inside the container, so the image is saved directly in your current directory on the host.

## Setup & Running

### 1. Clone the Repository

Open your terminal (Command Prompt/PowerShell on Windows or Terminal on Linux/macOS) and run:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Run Docer-Compose build command

- For Windows
```bash
$env:LINKEDIN_EMAIL="your-email@example.com"; $env:LINKEDIN_PASSWORD="your-password"; docker-compose up --build
```
- For Linux/MacOS
```bash
LINKEDIN_EMAIL="your-email@example.com" LINKEDIN_PASSWORD="your-password" docker-compose up --build
```