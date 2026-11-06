# Read config and dashboard in the source

**Lesson ID:** `social-media-sentiment-dashboard-module-05-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/config.py] and [src/dashboard.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include load_config, create_dashboard_app, update_dashboard; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/config.py`, `src/dashboard.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/config.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/config.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def load_config(config_path: str = None) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/dashboard.py`, `import dash` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/dashboard.py`, `from dash import dcc, html` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/dashboard.py`, `from dash.dependencies import Input, Output` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/dashboard.py`, `import plotly.graph_objs as go` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/dashboard.py`, `import random` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def create_dashboard_app(config):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def update_dashboard(n):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/config.py

```text
import json
import os

def load_config(config_path: str = None) -> dict:
    """
    Load social accounts configuration from a JSON file.
    """
    if not config_path:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "..", "config", "social_accounts.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
```

### src/dashboard.py

```text
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
import datetime
from utils import setup_logger

# In-memory store for simulated metrics (will update on each callback)
METRICS_STORE = {
    "twitter": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "facebook": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "instagram": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "discord": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "medium": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "reddit": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "youtube": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "tiktok": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)}
}

def create_dashboard_app(config):
    """
    Create and configure the Dash dashboard application.
    """
    app = dash.Dash(__name__)
    app.title = "social-metrics-dashboard Dashboard"

    app.layout = html.Div([
        html.H1("Social Media Analytics Dashboard", style={'textAlign': 'center'}),
        html.Div(id='last-update', children="Last update: " + str(datetime.datetime.now()), style={'textAlign': 'center', 'marginBottom': '20px'}),
        dcc.Interval(
            id='interval-component',
            interval=5*60*1000,  # every 5 minutes
            n_intervals=0
        ),
        html.Div([
            dcc.Graph(id='engagement-graph')
        ], style={'width': '80%', 'margin': 'auto'}),
        html.Br(),
        html.Div([
            dcc.Graph(id='sentiment-graph')
        ], style={'width': '80%', 'margin': 'auto'}),
        html.Br(),
        html.Div(id='metrics-table', style={'width': '60%', 'margin': 'auto'})
    ], style={'margin': '2%'})

    @app.callback(
        [Output('engagement-graph', 'figure'),
         Output('sentiment-graph', 'figure'),
         Output('last-update', 'children'),
         Output('metrics-table', 'children')],
        [Input('interval-component', 'n_intervals')]
    )
    def update_dashboard(n):
        # Simulate updating metrics with new random data.
        updated_metrics = {}
        for platform in METRICS_STORE.keys():
            updated_metrics[platform] = {
                "engagement": random.randint(100, 1000),
                "sentiment": round(random.uniform(-1, 1), 2)
            }
        METRICS_STORE.update(updated_metrics)
        last_update = "Last update: " + str(datetime.datetime.now())
        
        # Engagement bar chart
        platforms = list(METRICS_STORE.keys())
        engagements = [METRICS_STORE[platform]["engagement"] for platform in platforms]
        engagement_fig = {
            'data': [go.Bar(
                x=platforms,
                y=engagements,
                marker=dict(color='rgb(55, 83, 109)')
            )],
            'layout': go.Layout(
                title='Engagement Metrics by Platform',
                xaxis={'title': 'Platform'},
                yaxis={'title': 'Engagement'}
            )
        }
        
        # Sentiment distribution bar chart
        sentiments = [METRICS_STORE[platform]["sentiment"] for platform in platforms]
        sentiment_fig = {
            'data': [go.Bar(
                x=platforms,
                y=sentiments,
                marker=dict(color='rgb(26, 118, 255)')
            )],
            'layout': go.Layout(
                title='Average Sentiment Score by Platform',
                xaxis={'title': 'Platform'},
                yaxis={'title': 'Sentiment Score'}
            )
        }
        
        # Metrics table creation
        table_rows = []
        for platform, data in METRICS_STORE.items():
            table_rows.append(
                html.Tr([
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

This lesson ties its explanation to `src/config.py`, `src/dashboard.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
