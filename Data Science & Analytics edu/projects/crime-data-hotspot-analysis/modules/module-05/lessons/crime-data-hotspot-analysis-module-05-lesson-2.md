# Read code review and safe change 5 in the source

**Lesson ID:** `crime-data-hotspot-analysis-module-05-lesson-2`

## Purpose and learning objectives

Use EDA.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `EDA.py`, `app.py`, `clustering_analysis.py`, `dimensionality_reduction.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `dimensionality_reduction.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dimensionality_reduction.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dimensionality_reduction.py`, `from sklearn.decomposition import PCA` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dimensionality_reduction.py`, `from sklearn.manifold import TSNE` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dimensionality_reduction.py`, `from sklearn.preprocessing import StandardScaler` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def prepare_features(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def apply_pca(X_scaled, feature_cols, n_components=3):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def visualize_pca(X_pca, df, sample_size=10000):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def apply_tsne(X_scaled, df, sample_size=10000, perplexity=30):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### dimensionality_reduction.py

```text
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow

def prepare_features(df):
    """
    Prepare features for dimensionality reduction
    """
    feature_cols = ['Latitude', 'Longitude', 'Hour', 'Month', 'Is_Weekend',
                    'Crime_Severity_Score', 'Crime_Type_Encoded', 
                    'Location_Desc_Encoded']
    
    # Add day of week encoding
    df['Day_of_Week_Encoded'] = pd.factorize(df['Day_of_Week'])[0]
    feature_cols.append('Day_of_Week_Encoded')
    
    X = df[feature_cols].copy()
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, feature_cols

def apply_pca(X_scaled, feature_cols, n_components=3):
    """
    Apply PCA for dimensionality reduction
    """
    print("\n" + "="*50)
    print("PCA - Principal Component Analysis")
    print("="*50)
    
    # Full PCA to see explained variance
    pca_full = PCA()
    pca_full.fit(X_scaled)
    
    # Scree plot
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(pca_full.explained_variance_ratio_) + 1),
             np.cumsum(pca_full.explained_variance_ratio_), marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('PCA Explained Variance')
    plt.grid(True)
    plt.axhline(y=0.7, color='r', linestyle='--', label='70% threshold')
    plt.axhline(y=0.8, color='g', linestyle='--', label='80% threshold')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.bar(range(1, min(11, len(pca_full.explained_variance_ratio_) + 1)),
            pca_full.explained_variance_ratio_[:10])
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('Individual Component Variance')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pca_variance_analysis.png', dpi=300)
    plt.close()
    
    # Apply PCA with n_components
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    explained_var = sum(pca.explained_variance_ratio_)
    print(f"Components: {n_components}")
    print(f"Total Explained Variance: {explained_var:.4f} ({explained_var*100:.2f}%)")
    print(f"\nIndividual Component Variance:")
    for i, var in enumerate(pca.explained_variance_ratio_):
        print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")
    
    # Feature importance
    print(f"\nTop Features by Importance (PC1):")
    feature_importance = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': np.abs(pca.components_[0])
    }).sort_values('Importance', ascending=False)
    print(feature_importance.head(5))
    
    # Log to MLflow
    with mlflow.start_run(run_name="PCA_Analysis"):
        mlflow.log_param("n_components", n_components)
        mlflow.log_metric("explained_variance", explained_var)
        for i, var in enumerate(pca.explained_variance_ratio_):
            mlflow.log_metric(f"pc{i+1}_variance", var)
        mlflow.log_artifact('pca_variance_analysis.png')
    
    return X_pca, pca

def visualize_pca(X_pca, df, sample_size=10000):
    """
    Visualize PCA results
    """
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

This lesson ties its explanation to `EDA.py`, `app.py`, `clustering_analysis.py`, `dimensionality_reduction.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
