# Read declared dependencies and runtime configuration in the source

**Lesson ID:** `automated-eda-tool-module-20-lesson-2`

## Purpose and learning objectives

Inspect the actual manifests .github/workflows/ci.yml, backend/DOCKERFILE, backend/docker-compose.yml, backend/requirements.txt. Separate declared packages/settings from imports, installed state, secrets, and runtime success.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.github/workflows/ci.yml`, `backend/DOCKERFILE`, `backend/docker-compose.yml`, `backend/requirements.txt`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `backend/DOCKERFILE` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `backend/docker-compose.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `backend/requirements.txt` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .github/workflows/ci.yml

```text
name: CI - Python Lint and React Build

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8

    - name: Run flake8
      run: |
        flake8 autoeda --ignore=E501

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install npm dependencies
      run: npm install
      working-directory: frontend  

    - name: Run React build
      run: npm run build
      working-directory: frontend

```

### backend/DOCKERFILE

```text
# /backend/Dockerfile

# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

```

### backend/docker-compose.yml

```text
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    environment:
      - MONGO_INITDB_DATABASE=autoeda

volumes:
  mongodb_data:
```

### backend/requirements.txt

```text
Flask>=2.0.0
Werkzeug==3.0.4
pandas==1.5.3
numpy==1.24.0
scikit-learn==1.2.0
flask-cors==3.0.10  # Optional: If your frontend will access the API

```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `.github/workflows/ci.yml`, `backend/DOCKERFILE`, `backend/docker-compose.yml`, `backend/requirements.txt`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### backend/app.py

### backend/app.py

```text
from flask import Flask, request, jsonify, Response
import pandas as pd
from flask_cors import CORS
import chardet
import re
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import timedelta
import uuid
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from autoeda.summary_stats import summarize_csv

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "fallback_secret_key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

mongo_uri = os.getenv("MONGODB_URI") # Ensure you have set this in your .env file
mongo_client = MongoClient(mongo_uri)
db = mongo_client["auto-eda-backend"] #Change to your database name
users_collection = db.users

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://auto-eda-automated-data-preprocessing-toolkit.vercel.app"
]

CORS(app, resources={
    r"/upload": {"origins": ALLOWED_ORIGINS},
    r"/login": {"origins": ALLOWED_ORIGINS},
    r"/signup": {"origins": ALLOWED_ORIGINS},
    r"/me": {"origins": ALLOWED_ORIGINS},
    r"/contact": {"origins": ALLOWED_ORIGINS}, 
    r"/upload_csv": {"origins": ALLOWED_ORIGINS},
}, supports_credentials=True)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(c.isalpha() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

# Validate contact us from input
def validate_contact_form(data):
    errors = []
    if not data.get('name') or len(data.get('name', '').strip()) < 2:
        errors.append("Name must be at least 2 characters long")
    if not data.get('email') or not is_valid_email(data.get('email', '')):
        errors.append("Please provide a valid email address")
    if not data.get('subject') or len(data.get('subject', '').strip()) < 3:
        errors.append("Subject must be at least 3 characters long")
    if not data.get('message') or len(data.get('message', '').strip()) < 10:
        errors.append("Message must be at least 10 characters long")
    return errors

# Add this new endpoint
@app.route('/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    
    # Validate the form data
    validation_errors = validate_contact_form(data)
    if validation_errors:
        return jsonify({
            'status': 'error',
            'message': 'Validation failed',
            'errors': validation_errors
        }), 400
    
    try:
        # Store the contact submission in MongoDB
        contact_submission = {
            'name': data['name'].strip(),
            'email': data['email'].lower().strip(),
            'subject': data['subject'].strip(),
            'message': data['message'].strip(),
            'submitted_at': pd.Timestamp.now().isoformat(),
            'status': 'new'
        }
        
        # Insert into MongoDB
        db.contact_submissions.insert_one(contact_submission)
        
        return jsonify({
```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
