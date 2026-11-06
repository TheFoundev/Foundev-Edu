# Read app and feature selector in the source

**Lesson ID:** `automated-eda-tool-module-01-lesson-2`

## Purpose and learning objectives

Study the implementation in [backend/app.py] and [autoeda/feature_selector.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include is_valid_email, is_strong_password, validate_contact_form, handle_contact, signup, remove_low_variance, remove_highly_correlated; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `backend/app.py`, `autoeda/feature_selector.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `backend/app.py`, `from flask import Flask, request, jsonify, Response` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/app.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/app.py`, `from flask_cors import CORS` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/app.py`, `import chardet` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/app.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def is_valid_email(email):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def is_strong_password(password):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def validate_contact_form(data):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle_contact():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def signup():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def login():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/feature_selector.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feature_selector.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feature_selector.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feature_selector.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feature_selector.py`, `from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def remove_highly_correlated(` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def select_by_model_importance(` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### autoeda/feature_selector.py

```text
import pandas as pd
import numpy as np
import logging
import os
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.impute import SimpleImputer


# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Ensure output directory exists globally for all functions
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
log_file_path = os.path.join(output_dir, "feature_selection_log.txt")


def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Removes features from a DataFrame with variance below a given threshold.
    (Existing docstring and code)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input 'df' must be a pandas DataFrame.")
    if not isinstance(threshold, (int, float)):
        raise TypeError("Input 'threshold' must be a numeric value.")
    if threshold < 0:
        raise ValueError("Input 'threshold' must be non-negative.")

    numeric_cols_df = df.select_dtypes(include=np.number)
    if numeric_cols_df.empty:
        logging.info(
            "No numeric columns found to calculate variance in remove_low_variance.")
        with open(log_file_path, "a") as f:
            f.write(f"Timestamp: {pd.Timestamp.now()}\n")
            f.write("Function: remove_low_variance\n")
            f.write(f"Parameters: threshold={threshold}\n")
            f.write("Action: No numeric columns found. No features removed.\n\n")
        return df

    variances = numeric_cols_df.var()
    low_variance_features = variances[variances < threshold].index.tolist()

    original_feature_count = len(df.columns)
    df_filtered = df.drop(columns=low_variance_features, errors='ignore')
    removed_count = len(low_variance_features)

    if removed_count > 0:
        log_message = f"remove_low_variance: Removed {removed_count} features with variance below {threshold}: {low_variance_features}"
        logging.info(log_message)
        with open(log_file_path, "a") as f:
            f.write(f"Timestamp: {pd.Timestamp.now()}\n")
            f.write("Function: remove_low_variance\n")
            f.write(f"Parameters: threshold={threshold}\n")
            f.write(f"Original feature count: {original_feature_count}\n")
            f.write(f"Removed feature count: {removed_count}\n")
            f.write(f"Removed features: {low_variance_features}\n\n")
    else:
        logging.info(
            f"remove_low_variance: No features removed with threshold {threshold}.")
        with open(log_file_path, "a") as f:
            f.write(f"Timestamp: {pd.Timestamp.now()}\n")
            f.write("Function: remove_low_variance\n")
            f.write(f"Parameters: threshold={threshold}\n")
            f.write(
                "Action: No features met the low variance criteria. No features removed.\n\n")
    return df_filtered


def remove_highly_correlated(
        df: pd.DataFrame,
        threshold: float) -> pd.DataFrame:
    """
    Removes one feature from each pair of highly correlated features.
    (Existing docstring and code)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input 'df' must be a pandas DataFrame.")
    if not isinstance(threshold, (int, float)):
        raise TypeError("Input 'threshold' must be a numeric value.")
    if not 0 <= threshold <= 1:
        raise ValueError("Input 'threshold' must be between 0 and 1.")

    numeric_df = df.select_dtypes(include=np.number)
    if numeric_df.shape[1] < 2:
        logging.info(
            "remove_highly_correlated: Not enough numeric features to calculate correlation.")
        with open(log_file_path, "a") as f:
            f.write(f"Timestamp: {pd.Timestamp.now()}\n")
            f.write("Function: remove_highly_correlated\n")
            f.write(f"Parameters: threshold={threshold}\n")
            f.write(
                f"Action: Not enough numeric features ({nume
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

This lesson ties its explanation to `backend/app.py`, `autoeda/feature_selector.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
