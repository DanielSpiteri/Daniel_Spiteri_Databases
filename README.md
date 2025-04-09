This project is a simple FastAPI web application that allows users to upload multimedia content (sprites and audio files) and submit game scores to a MongoDB Atlas database. It was developed as part of the Home Assignment and covers all setup, database integration, and local testing steps.

Tools and Technologies Used
FastAPI: A modern, high-performance web framework for building APIs with Python.

Pydantic: For validating incoming data types, such as ensuring the player score is an integer.

Motor: An async driver for working with MongoDB in Python.

MongoDB Atlas: A cloud-hosted NoSQL database used to store uploaded files and player scores.

Visual Studio / VS Code: Used as the development environment.

Uvicorn: ASGI server to run the application locally.

Vercel: Attempted for deployment, but due to compatibility issues with ASGI and MongoDB, the API is currently only functioning locally.

How the Application Was Set Up
A virtual environment was created locally to manage dependencies: python -m venv .env

The environment was activated using: .\.env\Scripts\activate

All required libraries were installed using: pip install -r requirements.txt

The MongoDB connection string (with the database username and password) was added to a .env file to keep credentials secure: MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/

The server was run using: uvicorn main:app --reload

The API was accessed and tested on the browser at: http://127.0.0.1:8000/docs

MongoDB Atlas Configuration
A cluster was created on MongoDB Atlas.

A user (spiteridl) was set up with readWriteAnyDatabase permissions.

IP Whitelisting was configured to allow access from any IP (0.0.0.0/0) and my current IP address to ensure proper connectivity.

The database used was multimedia_db, which contains three collections: scores, audio, and sprites.

API Endpoints
GET / – Returns a welcome message to confirm the API is running.

POST /upload_sprite – Accepts a file upload and stores sprite data in MongoDB.

POST /upload_audio – Accepts an audio file upload and stores it.

POST /player_score – Accepts a player name and score (validated using Pydantic).

GET /player_scores – Returns a list of all player scores stored in the database.

Security and Injection Protection
To prevent malicious input (e.g., SQL or script injections), Pydantic models were used to validate inputs for each route. For example, the player_score route accepts only a string for player_name and an integer for score. This helps ensure that only correctly structured data can enter the database.

Additionally, by not using raw query strings or building queries from user input manually, the application avoids injection vulnerabilities. MongoDB itself is a NoSQL database, so it's inherently immune to classic SQL injection attacks.

Notes on Deployment
A vercel.json configuration file was created and added to the project to prepare for deployment using Vercel. However, due to technical issues with ASGI deployment on Vercel, the application is currently only running and tested locally.

If deployment is successful later on, a public URL will be added here.

This project demonstrates how to build, test, and connect a FastAPI-based application to MongoDB, along with basic API features like file uploads and score submission.

 “The app was tested locally using Swagger UI and an attempt was made to deploy it via Vercel. While the deployment did not fully succeed (404 error), all code and APIs function correctly in the local environment.”