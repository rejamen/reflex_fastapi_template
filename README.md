# Reflex and FastAPI Dockerized Project

This repository demonstrates a full-stack web application using **Reflex** for the frontend and **FastAPI** for the backend, all running in a Dockerized environment. The backend exposes a simple API, and the frontend interacts with it to display dynamic content.

---

## Project Structure
```
.
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── .web
|   ├── app
|   |    ├── __init__.py
|   |    ├── app.py
|   ├── assets
│   ├── Dockerfile
│   └── requirements.txt
│   ├── rxconfig.py
├── .env
├── .gitignore
└── docker-compose.yml
```

| File/Folder          | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `backend/`           | Directory containing the FastAPI backend code and dependencies.            |
| `backend/Dockerfile`  | Docker configuration file for setting up and running the FastAPI backend. |
| `backend/main.py`     | Main FastAPI application file defining routes and middleware.              |
| `backend/requirements.txt` | Python dependencies for the backend, including FastAPI and Uvicorn.    |
| `frontend/`               | Directory containing the Reflex frontend code and dependencies.            |
| `frontend/.web/`          | Auto-generated Reflex web files (should not be manually edited).           |
| `frontend/app/`           | Directory for the main application logic of the Reflex frontend.           |
| `frontend/app/__init__.py` | Initialization file for the `app` module.                                  |
| `frontend/app/app.py`     | Main Reflex application file for configuring the frontend app.             |
| `frontend/assets/`        | Directory for storing static assets like images, fonts, etc.              |
| `frontend/Dockerfile`     | Docker configuration file for setting up and running the Reflex frontend. |
| `frontend/requirements.txt` | Python dependencies for the Reflex frontend, including Reflex and aiohttp. |
| `frontend/rxconfig.py`    | Reflex configuration file for setting API URLs, ports, and other settings.|
| `.env`     | Env file to define some values needed for the frontend container. You should not push this file, but I did just for the example to be complete.
| `.gitignore`     | Git configuration file specifying files and folders to be ignored.
| `docker-compose.yml`     | Definition of the containers to run this project.



## Prerequisites

Make sure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/rejamen/reflex_fastapi_template.git &&
cd reflex_fastapi_template
```

### 2. Set your IP address in the `.env` file.
This is very important in order to make it possible the communication between the frontend and the endpoint in fastapi

### 3. Build and run the containers
Use Docker Compose to set up the backend and frontend:

```bash
docker-compose up --build
```


Wait until you see this result
```
INFO:     Started server process [1]
backend-1   | INFO:     Waiting for application startup.
backend-1   | INFO:     Application startup complete.
backend-1   | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
frontend-1  | ─────────────────────────────── Initializing app ───────────────────────────────
frontend-1  | [12:21:03] Initializing the web directory.                        console.py:104
frontend-1  | Success: Initialized app
frontend-1  | ───────────────────────────── Starting Reflex App ──────────────────────────────
frontend-1  | DeprecationWarning: Support for Python 3.9 and older has been deprecated in 
frontend-1  | version 0.6.0 please upgrade to Python 3.10 or newer. It will be completely 
frontend-1  | removed in 0.7.0
frontend-1  | INFO:app.app:Rendering index page
frontend-1  | [12:21:09] Compiling: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 13/13 0:00:00
frontend-1  | INFO:httpx:HTTP Request: POST https://app.posthog.com/capture/ "HTTP/1.1 200 OK"
frontend-1  | ───────────────────────────────── App Running ──────────────────────────────────
frontend-1  | App running at: http://localhost:3000
frontend-1  | Backend running at: http://0.0.0.0:3100
```

### 4. Access the application
* Frontend: http://localhost:3000
* Backend: http://localhost:8000/docs (API Documentation)

## Test the application
Once you access to http://localhost:3000 you should see a button 'Get Message'. Clicking on this button will show you a message "Hello from FastAPI backend!

## Next steps
* Modifiy the file `backend/main.py` to add/update your fastapi logic
* Modify the file `frontend/app/app.py` to add/update your frontend logic using Reflex

## Troubleshooting
* Ensure Docker is running and the required ports (3000, 3100, 8000) are available.
* Verify the dependencies in requirements.txt for both frontend and backend.
* Reflex uses websocket connection to sync its frontend and its backend (do not confuse this backend with your fastapi backend). If you see some issue, please check the Network Tab in your browser console, and filter for `WS` and be sure there are no issues there