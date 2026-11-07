# Architecture — Algorithmic Trading Signals

## Component map

main.py → src/data.py (make_prices, load_data) → src/model.py (rsi, add_features, forward_returns, train) → web/api_impl.py (summary)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

- `README.md`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/model.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`
- `web/server.py`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- Prices are simulated; results say nothing about real markets.
- The backtest ignores fees, slippage, position sizing and short selling.
- A real study needs walk-forward validation, multiple assets and proper risk controls.
