# Read documented goals mapped to implementation in the source

**Lesson ID:** `crime-data-hotspot-analysis-module-04-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors EDA.py, app.py, clustering_analysis.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `EDA.py`, `app.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `README.md`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `README.md`, `from sklearn.preprocessing import StandardScaler` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `README.md`, `from sklearn.cluster import KMeans` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `README.md`, `from sklearn.decomposition import PCA` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `README.md`, `from sklearn.manifold import TSNE` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `EDA.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `EDA.py`, `import matplotlib.pyplot as plt` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `EDA.py`, `import seaborn as sns` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `EDA.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def load_preprocessed_data():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def perform_eda(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def create_eda_visualizations(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `app.py`, `import streamlit as st` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import plotly.express as px` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import plotly.graph_objects as go` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def load_data():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text
# 🚨 Chicago Crime PatrolIQ - AI-Powered Crime Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)](https://plotly.com/)

> **Advanced unsupervised learning system analyzing 7M+ Chicago crime records to identify crime hotspots, patterns, and temporal trends.**

**GUVI Data Science Capstone Project 2025** | **Production-Ready** | **2 Contributors**

---

## 🎯 Problem Statement

Chicago experiences hundreds of thousands of crime incidents annually. Traditional crime analysis relies on:
- Manual pattern identification (time-consuming and error-prone)
- Limited temporal/spatial insights
- Difficulty identifying emerging crime hotspots
- No proactive resource allocation mechanism

**PatrolIQ solves this** by applying advanced unsupervised learning to discover hidden patterns in 7M+ historical crime records.

---

## ✨ Key Features

### 🧠 Machine Learning Intelligence
- **K-Means Clustering**: Identifies 5 distinct crime hotspots across Chicago
- **Dimensionality Reduction**: PCA & t-SNE for visualizing high-dimensional crime data
- **Elbow Method**: Automatic optimal cluster detection
- **Unsupervised Learning**: Discover patterns without labeled data

### 📊 Interactive Dashboard
- **Real-time Hotspot Mapping**: Geographic visualization of crime clusters
- **Temporal Analysis**: Crime trends across months/years
- **Elbow Curve Visualization**: Model optimization metrics
- **Dendrogram Analysis**: Hierarchical clustering insights
- **Dark Green Theme**: Professional, eye-friendly interface

### 📈 Advanced Visualizations
- K-Means clustering scatter plots (geographic coordinates)
- Elbow curves for optimal k determination
- Hierarchical dendrograms for cluster relationships
- Temporal crime distribution charts
- PCA/t-SNE dimensionality reduction plots

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|----------|
| **Data Processing** | Pandas, NumPy | Data cleaning & manipulation (7M+ records) |
| **Machine Learning** | scikit-learn | K-Means, PCA, t-SNE algorithms |
| **Visualization** | Plotly, Matplotlib | Interactive & static charts |
| **Frontend** | Streamlit | Production dashboard |
| **Data Storage** | CSV (chicago_crimes_final.csv) | Historical crime records |
| **Compute** | Python 3.9+ | Execution environment |

---

## 📊 Dataset

**Chicago Crime Data (2015-2025)**
- **Records**: 7M+ crime incidents
- **Features**: Coordinates (Lat/Long), Crime Type, Date, Location, Arrest Status
- **Source**: Chicago Police Department
- **File**: `chicago_crimes_final.csv`

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
pip or conda
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arun709/Chicago_crime_patrolIQ.git
   cd Chicago_crime_patrolIQ
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
```

### EDA.py

```text
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_preprocessed_data():
    """Load preprocessed data"""
    return pd.read_csv('chicago_crimes_preprocessed.csv')

def perform_eda(df):
    """
    Comprehensive exploratory data analysis
    """
    print("="*50)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    # Basic statistics
    print("\n1. DATASET OVERVIEW")
    print(f"Total Records: {len(df)}")
    print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nColumns: {df.columns.tolist()}")
    
    # Crime type distribution
    print("\n2. CRIME TYPE DISTRIBUTION")
    crime_counts = df['Primary Type'].value_counts()
    print(crime_counts.head(10))
    
    # Arrest rate
    arrest_rate = (df['Arrest'].sum() / len(df)) * 100
    print(f"\n3. ARREST RATE: {arrest_rate:.2f}%")
    
    # Domestic violence rate
    domestic_rate = (df['Domestic'].sum() / len(df)) * 100
    print(f"4. DOMESTIC VIOLENCE RATE: {domestic_rate:.2f}%")
    
    # Temporal patterns
    print("\n5. TEMPORAL PATTERNS")
    print(f"Crimes by Hour:\n{df['Hour'].value_counts().sort_index().head(10)}")
    print(f"\nCrimes by Day:\n{df['Day_of_Week'].value_counts()}")
    print(f"\nCrimes by Month:\n{df['Month'].value_counts().sort_index()}")
    
    return df

def create_eda_visualizations(df):
    """
    Create EDA visualizations
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    # 1. Top 10 Crime Types
    crime_counts = df['Primary Type'].value_counts().head(10)
    axes[0, 0].barh(crime_counts.index, crime_counts.values, color='steelblue')
    axes[0, 0].set_xlabel('Number of Crimes')
    axes[0, 0].set_title('Top 10 Crime Types')
    axes[0, 0].invert_yaxis()
    
    # 2. Crimes by Hour
    hourly_crimes = df['Hour'].value_counts().sort_index()
    axes[0, 1].plot(hourly_crimes.index, hourly_crimes.values, marker='o', color='crimson')
    axes[0, 1].set_xlabel('Hour of Day')
    axes[0, 1].set_ylabel('Number of Crimes')
    axes[0, 1].set_title('Crimes by Hour of Day')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Crimes by Day of Week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_crimes = df['Day_of_Week'].value_counts().reindex(day_order)
    axes[0, 2].bar(range(7), day_crimes.values, color='orange')
    axes[0, 2].set_xticks(range(7))
    axes[0, 2].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    axes[0, 2].set_title('Crimes by Day of Week')
    
    # 4. Arrest Rate by Crime Type
    top_crimes = df['Primary Type'].value_counts().head(10).index
    arrest_rates = df[df['Primary Type'].isin(top_crimes)].groupby('Primary Type')['Arrest'].mean() * 100
    axes[1, 0].barh(arrest_rates.index, arrest_rates.values, color='green')
    axes[1, 0].set_xlabel('Arrest Rate (%)')
    axes[1, 0].set_title('Arrest Rate by Crime Type')
    axes[1, 0].invert_yaxis()
    
    # 5. Monthly Crime Trend
    monthly_crimes = df['Month'].value_counts().sort_index()
    axes[1, 1].plot(monthly_crimes.index, monthly_crimes.values, marker='s', color='purple')
    axes[1, 1].set_xlabel('Month')
    axes[1, 1].set_ylabel('Number of Crimes')
    axes[1, 1].set_title('Monthly Crime Distribution')
    axes[1, 1].grid(True, alpha=0.3)
    
    # 6. Geographic Distribution (Heatmap style scatter)
    sample = df.sample(n=min(10000, len(df)))
    axes[1, 2].scatter(sample['Longitude'], sample['Latitude'], 
                      c=sample['Crime_Severity_Score'], cmap='YlOrRd', 
                      alpha=0.3, s=1)
    axes[1, 2].set_xlabel('Longitude')
    axes[1, 2].set_ylabel('Latitude')
    axes[1, 2].set_title('Geographic Crime Distribution')
    
    plt.tight_layout()
    plt.savefig('eda_visualizations.png', dpi=300, bbox_inches='tight')
```

### app.py

```text
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="PatrolIQ - Smart Safety Analytics",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - WORLD-CLASS DARK THEME
# ============================================================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d3f 50%, #0a0e27 100%);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1729 0%, #1a1f3a 100%);
        border-right: 2px solid rgba(99, 102, 241, 0.3);
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.5);
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }
    
    /* Main Title */
    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #a0aec0;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(99, 102, 241, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4);
        border-color: rgba(99, 102, 241, 0.6);
    }
    
    .kpi-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #64748b;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
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

This lesson ties its explanation to `README.md`, `EDA.py`, `app.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
