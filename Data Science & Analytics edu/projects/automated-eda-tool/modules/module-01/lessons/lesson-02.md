# API and Feature Selection: Trace the code

**Lesson ID:** `automated-eda-tool-module-01-lesson-02`  
**Module ID:** `automated-eda-tool-module-01`  
**Source focus:** `backend/app.py` → `is_valid_email`

## Purpose and learning objectives

Trace `is_valid_email` in `backend/app.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: App and Feature Selector.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `backend/app.py` and locate `is_valid_email`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `backend/app.py`, `autoeda/feature_selector.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `backend/app.py`. source tree absent; excerpt retained from earlier package

### backend/app.py

The excerpt below is the selected implementation focus.
### autoeda/feature_selector.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

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
    if not data.get('subject') or len(data.get('subject', '').str
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-01.md`](../exercises/exercise-01.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `is_valid_email` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `is_valid_email` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
