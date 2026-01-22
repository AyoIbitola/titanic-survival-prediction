# Deployment Guide

This guide will help you deploy your **Titanic Survival Prediction** app to a cloud platform.

## Option 1: Render.com (Recommended)

1.  **Push to GitHub**:
    - Create a new repository on GitHub (e.g., `titanic-survival-prediction`).
    - Upload all files from `Titanic_Project_AyomideIbitola_23CG034077` to this repository.
    - Ensure `requirements.txt` is in the root of the repo.

2.  **Create Web Service on Render**:
    - Go to [dashboard.render.com](https://dashboard.render.com/).
    - Click **New +** -> **Web Service**.
    - Connect your GitHub account and select your new repository.

3.  **Configure Settings**:
    - **Name**: `titanic-survival-app`.
    - **Runtime**: `Python 3`.
    - **Build Command**: `pip install -r requirements.txt`.
    - **Start Command**: `gunicorn app:app`.

4.  **Deploy**:
    - Click **Create Web Service**.
    - Wait for the URL.

5.  **Final Step**:
    - Copy the URL into `Titanic_hosted_webGUI_link.txt`.

## Option 2: PythonAnywhere

1.  **Upload Files**: to [pythonanywhere.com](https://www.pythonanywhere.com/).
2.  **Install Dependencies**:
    `pip install -r requirements.txt`
3.  **Configure Web App**:
    - Point to `/home/yourusername/Titanic_Project_AyomideIbitola_23CG034077/app.py`.
4.  **Reload** and test.
