# Architecture and source map

## Repository evidence

- `.github/workflows/ci.yml`
- `README.md`
- `autoeda/__init__.py`
- `autoeda/data_optimizer.py`
- `autoeda/encoding_categorical.py`
- `autoeda/feat_scaling.py`
- `autoeda/feature_selector.py`
- `autoeda/notebook_data_optimization.py`
- `autoeda/null_handler.py`
- `autoeda/outliers.py`
- `autoeda/pca_transformer.py`
- `autoeda/pipeline.py`
- `autoeda/summary_stats.py`
- `autoeda/test_notebook_data_optimization.py`
- `autoeda/test_null_handler.py`
- `backend/DOCKERFILE`
- `backend/README.md`
- `backend/app.py`
- `backend/config/database.js`
- `backend/docker-compose.yml`
- `backend/requirements.txt`
- `backend/router/file_router.py`
- `backend/services/run_data_optimization_test.py`
- `backend/services/runner.py`
- `docker-compose.yml`
- `frontend/DOCKERFILE`
- `frontend/README.md`
- `frontend/eslint.config.js`
- `frontend/package.json`
- `frontend/postcss.config.js`
- `frontend/src/App.jsx`
- `frontend/src/components/About.jsx`
- `frontend/src/components/Auth.jsx`
- `frontend/src/components/Contact.jsx`
- `frontend/src/components/Dashboard.jsx`
- `frontend/src/components/FileUpload.jsx`
- `frontend/src/components/Footer.jsx`
- `frontend/src/components/Home.jsx`
- `frontend/src/components/HowItWorks.jsx`
- `frontend/src/components/Navbar.jsx`
- `frontend/src/components/scrollCard.jsx`
- `frontend/src/components/theme-provider.jsx`
- `frontend/src/components/ui/button.jsx`
- `frontend/src/components/ui/card.jsx`
- `frontend/src/components/ui/input.jsx`
- `frontend/src/components/userProfile.jsx`
- `frontend/src/lib/utils.js`
- `frontend/src/main.jsx`
- `frontend/tailwind.config.js`
- `frontend/vite.config.js`
- `package.json`
- `run_cleaning.py`
- `unit_tests/__init__.py`
- `unit_tests/outlier_test.py`
- `unit_tests/test_data_optimizer.py`
- `unit_tests/test_encoding_categorical.py`
- `unit_tests/test_feat_scaling.py`
- `unit_tests/test_feature_selector.py`
- `unit_tests/test_pca_transformer.py`

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> <div align="center">
> 
> <picture>
>   <source media="(prefers-color-scheme: dark)" srcset="./frontend/src/components/Autd.svg" />
>   <source media="(prefers-color-scheme: light)" srcset="./frontend/src/components/Aut.svg" />
>   <img src="path/to/light-logo.png" alt="Project Logo" width="250" />
> </picture>
> 
> </div>
> 
> ---
> 
> # ⚡ AutoEDA - Automated Data Preprocessing Toolkit
> 
> ![GitHub repo size](https://img.shields.io/github/repo-size/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit?color=brightgreen)
> ![GitHub contributors](https://img.shields.io/github/contributors/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
> ![GitHub last commit](https://img.shields.io/github/last-commit/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
> ![Issues](https://img.shields.io/github/issues/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
> ![License](https://img.shields.io/github/license/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
> ![GitHub Stars](https://img.shields.io/github/stars/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit?style=flat-square)
> 
> > ⚡ Automate tedious data cleaning — focus more on insights, not pipelines.
> 
> ---
> 
> ## 📌 Table of Contents
> 
> * [🔍 Overview](#-overview)
> * [✨ Key Features](#-key-features)
> * [🧱 Project Architecture](#-project-architecture)
> * [📦 Requirements](#-requirements)
> * [🚀 Getting Started](#-getting-started)
> * [🤝 How to Contribute](#-how-to-contribute)
> * [🛡 License](#-license)
> * [📬 Contact](#-contact)
> 
> ## 🔍 Overview
> 
> AutoEDA is a lightweight yet powerful toolkit that streamlines data preprocessing for Exploratory Data Analysis (EDA) and Machine Learning.
> 
> It automates routine cleaning tasks such as missing value treatment, type correction, and feature engineering, helping data scientists and analysts unlock insights faster and with less friction.
> 
> ## ✨ Key Features
> 
> * ✅ Seamless CSV upload & schema validation
> * ✅ Null value imputation & type inference
> * ✅ Smart duplicate detection & cleanup
> * ✅ Feature extraction and transformation
> * ✅ REST API support for integration
> * ✅ Modern React + Vite frontend
> * ✅ Dockerized deployment for easy setup
> 
> ## 🧱 Project Architecture
> 
> ### 🧠 Backend (Python)
> 
> * Modular design for cleaning, transforming, and preprocessing datasets
> * Built with FastAPI for high-speed async REST APIs
> * Easily extendable for custom ML workflows
> 
> ### 🎨 Frontend (React + Vite)
> 
> * Sleek UI for uploading, previewing, and processing datasets
> * Designed for responsiveness and ease-of-use
> * Optional sections for documentation, help, and dataset history
> 
> ### 🐳 Docker Support
> 
> * Docker & Docker Compose configuration for cross-platform deployment
> * One command to launch the full app stack
> 
> ## 📦 Requirements
> 
> * 🧑‍💻 Frontend: React.js, Vite
> * 🐍 Backend: Python 3.x, FastAPI, Pandas
> * 🐳 Containerization: Docker & Docker Compose
> 
> > ⚠️ Remember to configure your `.gitignore` and environment variables!
> 
> ## 🚀 Getting Started
> 
> 1️⃣ **Clone the repository**
> 
> ```bash
> git clone https://github.com/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit
> cd AutoEDA-Automated-Data-Preprocessing-Toolkit
> ```
> 
> 2️⃣ **Run the backend**
> 
> ```bash
> cd backend
> pip install -r requirements.txt
> uvicorn main:app --reload
> ```
> 
> 3️⃣ **Launch the frontend**
> 
> ```bash
> cd frontend
> npm install
> npm run dev
> ```
> 
> 4️⃣ **\[Optional] Run everything with Docker**
> 
> ```bash
> docker-compose up --build
> ```
> 
> ## 🤝 How to Contribute
> 
> We 💖 community contributions! Here’s how you can make an impact:
> 
> ### 🔧 Frontend
> 
> *
> 
> ### 🧪 Model Pipeline
> 
> *
> 
> ### ⚙️ Backend
> 
> *
> 
> 📢 New to open source? Start here: [`CONTRIBUTING.md`](CONTRIBUTING.md)
> 
> ✨ Looking for ideas? Explore [Good First Issues](https://github.com/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit/labels/good%20first%20issue)
> 
> ## 🛡 License
> 
> This project uses a **Modified MIT License**.
> 
> 🔒 **Please read the ****`LICENSE`**** file** carefully before using or contributing.
> 
> ## 📬 Contact
> 
> We'd love to hear from you!
> 
> * 🗨 [Open an issue](https://github.com/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit/issues/new)
> * 🔁 [Submit a pull request](https://github.com/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit/pulls)
> * ⭐ Star the repo if you find it helpful
> 
> > Built with ❤️ by passionate developers — for the community, by the community.
> 
> ## ✨ If you found this project useful...
> 
> Please consider ⭐ starring the repository and sharing it with your team or on social media.
> 
> ---
> 
> > "Keep pushing boundaries — even small steps can lead to powerful transformations. 🌱"
> 
> > "Believe in the process, trust your curiosity, and let every dataset take you one step closer to mastery. 💡📊"
> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
