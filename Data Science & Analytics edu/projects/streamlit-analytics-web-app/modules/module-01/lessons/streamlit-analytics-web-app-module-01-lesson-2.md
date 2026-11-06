# Read app and main in the source

**Lesson ID:** `streamlit-analytics-web-app-module-01-lesson-2`

## Purpose and learning objectives

Study the implementation in [app.py] and [main.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include read_subscriptions, main; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `app.py`, `main.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `app.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import streamlit as st` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def read_subscriptions(data_dir: str) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import CURRENT_MONTH, cohort_retention, filter_data, load, mrr_by_month, save, summary` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""The subscription analytics page.

Run it with `streamlit run app.py`.
"""
from pathlib import Path

import pandas as pd
import streamlit as st

from src.pipeline import (
    CURRENT_MONTH,
    MONTHS,
    REGIONS,
    SEGMENTS,
    cohort_retention,
    filter_data,
    load,
    mrr_by_month,
    summary,
)

st.set_page_config(page_title="Subscription analytics", layout="wide")

DATA_DIR = Path(__file__).parent / "artifacts"


@st.cache_data(ttl=300)
def read_subscriptions(data_dir: str) -> pd.DataFrame:
    """The subscriptions, cached so the page is quick."""
    return load(data_dir)


st.title("Subscription analytics")
st.caption(
    "The MRR is the monthly fee of the subscriptions that are running in the month. "
    "The average fee is the MRR of the month divided by the number of active "
    "subscriptions, the churn is the share of the running subscriptions that "
    "ended in the month, and the net revenue retention says how much the "
    "customers that were already there brought in."
)

frame = read_subscriptions(str(DATA_DIR))

with st.sidebar:
    st.header("Filters")
    segment = st.selectbox("Segment", ["all"] + SEGMENTS)
    region = st.selectbox("Region", ["all"] + REGIONS)
    first = st.selectbox("From", MONTHS, index=0)
    last = st.selectbox("To", MONTHS, index=len(MONTHS) - 1)
    months = [month for month in MONTHS if MONTHS.index(month) >= MONTHS.index(first)
              and MONTHS.index(month) <= MONTHS.index(last)]
    st.divider()
    st.caption(f"{len(frame)} subscriptions in total")

filtered = filter_data(frame, segment, region, months)
numbers = summary(filtered, CURRENT_MONTH)

columns = st.columns(5)
columns[0].metric("MRR", f"{numbers['mrr']:,.2f}")
columns[1].metric("ARR", f"{numbers['arr']:,.2f}")
columns[2].metric("Active customers", numbers["active"])
columns[3].metric("Average fee", f"{numbers['average_fee']:,.2f}")
columns[4].metric("Churn", f"{numbers['churn_rate'] * 100:.1f}%")

left, right = st.columns(2)

with left:
    st.subheader("The revenue of every month")
    monthly = mrr_by_month(filtered, MONTHS)
    chart = monthly.set_index("month")[["mrr", "customers"]]
    st.line_chart(chart)

with right:
    st.subheader("The revenue by segment")
    if numbers["by_segment"]:
        st.bar_chart(pd.DataFrame(numbers["by_segment"]).set_index("segment")["mrr"])
    else:
        st.info("No subscription matches the filters.")

st.subheader("New customers, churned customers and the revenue of every month")
st.dataframe(
    monthly.rename(columns={
        "mrr": "MRR", "customers": "active", "new": "new", "churned": "churned",
    }),
    use_container_width=True,
)

st.subheader("How much of every cohort is still there")
cohorts = cohort_retention(filtered, MONTHS)
if not cohorts.empty:
    st.dataframe(cohorts.set_index("cohort"), use_container_width=True)
else:
    st.info("No cohort matches the filters.")

st.subheader("The customers")
st.dataframe(filtered.sort_values("monthly_fee", ascending=False), use_container_width=True)

st.download_button(
    "Download the subscriptions",
    filtered.to_csv(index=False).encode("utf-8"),
```

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import CURRENT_MONTH, cohort_retention, filter_data, load, mrr_by_month, save, summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Subscription analytics.")
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print("Subscription analytics with Streamlit.")
        print("Run `streamlit run app.py` for the page, or `python main.py run` for the numbers.")
        return

    if args.command == "demo":
        frame = load(base_dir=args.base_dir)
        numbers = summary(frame, CURRENT_MONTH)
        print(f"MRR: {numbers['mrr']:.2f}, ARR: {numbers['arr']:.2f}")
        print(f"Active customers: {numbers['active']}, average fee: {numbers['average_fee']:.2f}")
        print(f"Churn: {numbers['churn_rate'] * 100:.1f}%, net revenue retention: {numbers['net_revenue_retention'] * 100:.1f}%")
        print(mrr_by_month(frame).to_string(index=False))
        print(cohort_retention(frame).to_string(index=False))
        return

    frame = load(base_dir=args.base_dir)
    save(frame, base_dir=args.base_dir)
    print(json.dumps(summary(frame, CURRENT_MONTH), indent=2, default=str))


if __name__ == "__main__":
    main()

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

This lesson ties its explanation to `app.py`, `main.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
