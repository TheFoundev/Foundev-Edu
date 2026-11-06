# A beginner's model of app and clustering analysis

**Lesson ID:** `crime-data-hotspot-analysis-module-01-lesson-1`

## Purpose and learning objectives

Study the implementation in [app.py] and [clustering_analysis.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include prepare_clustering_data, geographic_kmeans_clustering, geographic_dbscan_clustering; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `app.py`, `clustering_analysis.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `app.py`, `import streamlit as st` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import plotly.express as px` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import plotly.graph_objects as go` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def load_data():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `clustering_analysis.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `clustering_analysis.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `clustering_analysis.py`, `from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `clustering_analysis.py`, `from sklearn.preprocessing import StandardScaler` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `clustering_analysis.py`, `from sklearn.metrics import silhouette_score, davies_bouldin_score` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def prepare_clustering_data(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def geographic_kmeans_clustering(geo_scaled, geo_features, n_clusters=7):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def geographic_dbscan_clustering(geo_scaled, geo_features, eps=0.05, min_samples=50):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def geographic_hierarchical_clustering(geo_scaled, geo_features, n_clusters=7):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def temporal_kmeans_clustering(temporal_scaled, n_clusters=5):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### clustering_analysis.py

```text
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import mlflow.sklearn

def prepare_clustering_data(df):
    """
    Prepare data for clustering
    """
    # Geographic features
    geo_features = df[['Latitude', 'Longitude']].copy()
    
    # Temporal features
    temporal_features = df[['Hour', 'Month', 'Day_of_Week', 'Is_Weekend']].copy()
    temporal_features['Day_of_Week'] = pd.factorize(temporal_features['Day_of_Week'])[0]
    
    # Normalize features
    scaler_geo = StandardScaler()
    scaler_temporal = StandardScaler()
    
    geo_scaled = scaler_geo.fit_transform(geo_features)
    temporal_scaled = scaler_temporal.fit_transform(temporal_features)
    
    return geo_scaled, temporal_scaled, geo_features, temporal_features

def geographic_kmeans_clustering(geo_scaled, geo_features, n_clusters=7):
    """
    K-Means clustering for geographic hotspots
    """
    print("\n" + "="*50)
    print("K-MEANS CLUSTERING - Geographic Hotspots")
    print("="*50)
    
    # Elbow method to find optimal k
    inertias = []
    silhouette_scores = []
    K_range = range(3, 11)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(geo_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(geo_scaled, kmeans.labels_))
    
    # Plot elbow curve
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(K_range, inertias, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(K_range, silhouette_scores, marker='o', color='orange')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score vs K')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('kmeans_elbow_analysis.png', dpi=300)
    plt.close()
    
    # Final clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(geo_scaled)
    
    # Evaluation metrics
    silhouette = silhouette_score(geo_scaled, labels)
    davies_bouldin = davies_bouldin_score(geo_scaled, labels)
    
    print(f"Number of Clusters: {n_clusters}")
    print(f"Silhouette Score: {silhouette:.4f}")
    print(f"Davies-Bouldin Index: {davies_bouldin:.4f}")
    
    # Log to MLflow
    with mlflow.start_run(run_name="KMeans_Geographic"):
        mlflow.log_param("algorithm", "KMeans")
        mlflow.log_param("n_clusters", n_clusters)
        mlflow.log_metric("silhouette_score", silhouette)
        mlflow.log_metric("davies_bouldin_index", davies_bouldin)
        mlflow.sklearn.log_model(kmeans, "model")
        mlflow.log_artifact('kmeans_elbow_analysis.png')
    
    # Visualize clusters
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(geo_features['Longitude'], geo_features['Latitude'], 
                         c=labels, cmap='viridis', alpha=0.3, s=1)
    plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 0], 
               c='red', marker='X', s=200, edgecolors='black', linewidths=2, 
               label='Centroids')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('K-Means Crime Hotspot Clusters')
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

This lesson ties its explanation to `app.py`, `clustering_analysis.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
