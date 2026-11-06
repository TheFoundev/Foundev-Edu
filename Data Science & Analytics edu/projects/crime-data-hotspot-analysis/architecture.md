# Architecture and source map

## Repository evidence

- `Data_preprocessing.py`
- `EDA.py`
- `README.md`
- `app.py`
- `clustering_analysis.py`
- `dimensionality_reduction.py`
- `requirements.txt`

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # 🚨 Chicago Crime PatrolIQ - AI-Powered Crime Intelligence Platform
> 
> [![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge)](https://www.python.org/)
> [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
> [![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge)](https://scikit-learn.org/)
> [![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)](https://plotly.com/)
> 
> > **Advanced unsupervised learning system analyzing 7M+ Chicago crime records to identify crime hotspots, patterns, and temporal trends.**
> 
> **GUVI Data Science Capstone Project 2025** | **Production-Ready** | **2 Contributors**
> 
> ---
> 
> ## 🎯 Problem Statement
> 
> Chicago experiences hundreds of thousands of crime incidents annually. Traditional crime analysis relies on:
> - Manual pattern identification (time-consuming and error-prone)
> - Limited temporal/spatial insights
> - Difficulty identifying emerging crime hotspots
> - No proactive resource allocation mechanism
> 
> **PatrolIQ solves this** by applying advanced unsupervised learning to discover hidden patterns in 7M+ historical crime records.
> 
> ---
> 
> ## ✨ Key Features
> 
> ### 🧠 Machine Learning Intelligence
> - **K-Means Clustering**: Identifies 5 distinct crime hotspots across Chicago
> - **Dimensionality Reduction**: PCA & t-SNE for visualizing high-dimensional crime data
> - **Elbow Method**: Automatic optimal cluster detection
> - **Unsupervised Learning**: Discover patterns without labeled data
> 
> ### 📊 Interactive Dashboard
> - **Real-time Hotspot Mapping**: Geographic visualization of crime clusters
> - **Temporal Analysis**: Crime trends across months/years
> - **Elbow Curve Visualization**: Model optimization metrics
> - **Dendrogram Analysis**: Hierarchical clustering insights
> - **Dark Green Theme**: Professional, eye-friendly interface
> 
> ### 📈 Advanced Visualizations
> - K-Means clustering scatter plots (geographic coordinates)
> - Elbow curves for optimal k determination
> - Hierarchical dendrograms for cluster relationships
> - Temporal crime distribution charts
> - PCA/t-SNE dimensionality reduction plots
> 
> ---
> 
> ## 🛠️ Tech Stack
> 
> | Component | Technology | Purpose |
> |-----------|-----------|----------|
> | **Data Processing** | Pandas, NumPy | Data cleaning & manipulation (7M+ records) |
> | **Machine Learning** | scikit-learn | K-Means, PCA, t-SNE algorithms |
> | **Visualization** | Plotly, Matplotlib | Interactive & static charts |
> | **Frontend** | Streamlit | Production dashboard |
> | **Data Storage** | CSV (chicago_crimes_final.csv) | Historical crime records |
> | **Compute** | Python 3.9+ | Execution environment |
> 
> ---
> 
> ## 📊 Dataset
> 
> **Chicago Crime Data (2015-2025)**
> - **Records**: 7M+ crime incidents
> - **Features**: Coordinates (Lat/Long), Crime Type, Date, Location, Arrest Status
> - **Source**: Chicago Police Department
> - **File**: `chicago_crimes_final.csv`
> 
> ---
> 
> ## 🚀 Quick Start
> 
> ### Prerequisites
> ```bash
> Python 3.9+
> pip or conda
> ```
> 
> ### Installation
> 
> 1. **Clone the repository**
>    ```bash
>    git clone https://github.com/Arun709/Chicago_crime_patrolIQ.git
>    cd Chicago_crime_patrolIQ
>    ```
> 
> 2. **Create virtual environment**
>    ```bash
>    # Windows
>    python -m venv venv
>    venv\Scripts\activate
>    
>    # Linux/Mac
>    python3 -m venv venv
>    source venv/bin/activate
>    ```
> 
> 3. **Install dependencies**
>    ```bash
>    pip install -r requirements.txt
>    ```
> 
> 4. **Run the Streamlit app**
>    ```bash
>    streamlit run app.py
>    ```
>    
>    Opens at: `http://localhost:8501`
> 
> ---
> 
> ## 📁 Project Structure
> 
> ```
> Chicago_crime_patrolIQ/
> ├── app.py                      # Streamlit dashboard
> ├── Data_preprocessing.py        # Data cleaning & preparation
> ├── clustering_analysis.py       # K-Means algorithm
> ├── dimensionality_reduction.py  # PCA & t-SNE
> ├── EDA.py                       # Exploratory Data Analysis
> ├── requirements.txt             # Dependencies
> ├── chicago_crimes_final.csv     # Dataset (7M+ records)
> ├── .gitignore                   # Ignore files
> │
> ├── Visualizations/              # Output charts
> │   ├── dbscan_geographic_clusters.png
> │   ├── kmeans_geographic_clusters.png
> │   ├── kmeans_elbow_analysis.png
> │   ├── hierarchical_dendrogram.png
> │   └── pca_variance_analysis.png
> │
> └── Documentation/
>     ├── README.md                # This file
>     └── Analysis_Report.pdf      # Detailed findings
> ```
> 
> ---
> 
> ## 🔬 Algorithm Details
> 
> ### K-Means Clustering
> - **Number of Clusters**: 5 (determined by elbow method)
> - **Features Used**: Latitude, Longitude (geographic coordinates)
> - **Convergence**: Typically <10 iterations
> - **Output**: Crime hotspot centroids & assignments
> 
> ### Dimensionality Reduction
> - **PCA**: Variance preservation = ~95% with 2-3 components
> - **t-SNE**: Perplexity=30, Iterations=1000 for cluster separation
> - **Purpose**: Visualize complex crime patterns in 2D space
> 
> ### Preprocessing
> - Remove missing coordinates (Lat/Long)
> - Normalize coordinates for consistent scale
> - Handle categorical features (crime type, arrest status)
> - Temporal binning (monthly/yearly aggregation)
> 
> ---
> 
> ## 📊 Key Findings
> 
> ✅ **5 Distinct Crime Hotspots Identified**
> - Downtown Chicago (highest concentration)
> - South Side clusters
> - West Side patterns
> - North Side incidents
> - Peripheral areas
> 
> ✅ **Temporal Patterns**
> - Seasonal crime variations
> - Peak incident times/months
> - Year-over-year trends
> 
> ✅ **Geographic Insights**
> - High-risk vs low-risk neighborhoods
> - Inter-cluster crime type differences
> - Resource allocation recommendations
> 
> ---
> 
> ## 🎓 ML Concepts Demonstrated
> 
> ✅ **Unsupervised Learning**: K-Means clustering without labels  
> ✅ **Dimensionality Reduction**: PCA for variance explained, t-SNE for visualization  
> ✅ **Exploratory Data Analysis**: Pattern recognition in 7M+ records  
> ✅ **Data Preprocessing**: Handling large datasets efficiently  
> ✅ **Model Evaluation**: Elbow method, silhouette analysis  
> ✅ **Interactive Dashboards**: Streamlit for real-time exploration  
> ✅ **Geospatial Analysis**: Geographic clustering & mapping  
> 
> ---
> 
> ## 💻 Code Walkthrough
> 
> ### 1. Data Loading & Preprocessing
> ```python
> import pandas as pd
> from sklearn.preprocessing import StandardScaler
> 
> # Load 7M+ crime records
> df = pd.read_csv('chicago_crimes_final.csv')
> 
> # Extract coordinates
> X = df[['Latitude', 'Longitude']].dropna()
> 
> # Normalize coordinates
> scaler = StandardScaler()
> X_scaled = scaler.fit_transform(X)
> ```
> 
> ### 2. K-Means Clustering
> ```python
> from sklearn.cluster import KMeans
> 
> # Fit K-Means with k=5
> kmeans = KMeans(n_clusters=5, random_state=42)
> clusters = kmeans.fit_predict(X_scaled)
> ```
> 
> ### 3. Dimensionality Reduction
> ```python
> from sklearn.decomposition import PCA
> from sklearn.manifold import TSNE
> 
> # PCA
> pca = PCA(n_components=2)
> X_pca = pca.fit_transform(X_scaled)
> 
> # t-SNE
> tsne = TSNE(n_components=2, random_state=42)
> X_tsne = tsne.fit_transform(X_scaled)
> ```
> 
> ### 4. Streamlit Visualization
> ```python
> import streamlit as st
> import plotly.express as px
> 
> st.set_page_config(page_title="Crime PatrolIQ", layout="wide")
> 
> # Geographic hotspot map
> fig = px.scatter(x=X_pca[:, 0], y=X_pca[:, 1], 
>                  color=clusters, title="Crime Hotspots")
> st.plotly_chart(fig, use_container_width=True)
> ```
> 
> ---
> 
> ## 📈 Results
> 
> | Metric | Value |
> |--------|-------|
> | **Records Analyzed** | 7M+ |
> | **Crime Hotspots Identified** | 5 clusters |
> | **Data Points in Largest Cluster** | ~2.5M |
> | **Geographic Coverage** | Entire Chicago |
> | **PCA Variance Explained** | 95%+ |
> | **Processing Time** | <60 seconds |
> | **Dashboard Response Time** | <2 seconds |
> 
> ---
> 
> ## 🔍 Use Cases
> 
> 1. **Police Resource Allocation**: Deploy officers to high-crime clusters
> 2. **Community Safety Planning**: Identify risk zones for prevention programs
> 3. **Urban Policy**: Data-driven decision making for city planning
> 4. **Insurance Risk Assessment**: Premium calculation by geographic cluster
> 5. **Research & Analysis**: Academic studies on urban crime patte

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
