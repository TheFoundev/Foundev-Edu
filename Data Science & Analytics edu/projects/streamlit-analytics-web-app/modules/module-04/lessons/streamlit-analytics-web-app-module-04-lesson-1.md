# A beginner's model of test code and evidence boundaries

**Lesson ID:** `streamlit-analytics-web-app-module-04-lesson-1`

## Purpose and learning objectives

Read test implementations tests/test_pipeline.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pytest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def subscriptions():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_subscription_is_active_from_its_start_month():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_subscription_stops_at_its_churn_month():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_mrr_is_the_sum_of_the_running_subscriptions(subscriptions):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_arr_is_twelve_months_of_mrr(subscriptions):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_average_fee_is_the_mrr_per_active_customer(subscriptions):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_pipeline.py

```text
"""Tests for the subscription metrics."""
import pandas as pd
import pytest

from src.pipeline import (
    CURRENT_MONTH,
    MONTHS,
    active_in,
    cohort_retention,
    filter_data,
    is_active,
    load,
    make_subscriptions,
    mrr_by_month,
    save,
    summary,
)


@pytest.fixture()
def subscriptions():
    return make_subscriptions(count=60, seed=5)


def test_a_subscription_is_active_from_its_start_month():
    row = {"start_month": "2026-01", "churn_month": None}
    assert is_active(row, "2025-12") is False
    assert is_active(row, "2026-01") is True
    assert is_active(row, "2026-04") is True


def test_a_subscription_stops_at_its_churn_month():
    row = {"start_month": "2026-01", "churn_month": "2026-03"}
    assert is_active(row, "2026-02") is True
    assert is_active(row, "2026-03") is False
    assert is_active(row, "2026-04") is False


def test_the_mrr_is_the_sum_of_the_running_subscriptions(subscriptions):
    frame = active_in(subscriptions, CURRENT_MONTH)
    expected = round(float(frame["monthly_fee"].sum()), 2)
    assert summary(subscriptions)["mrr"] == expected


def test_the_arr_is_twelve_months_of_mrr(subscriptions):
    numbers = summary(subscriptions)
    assert numbers["arr"] == round(numbers["mrr"] * 12, 2)


def test_the_average_fee_is_the_mrr_per_active_customer(subscriptions):
    numbers = summary(subscriptions)
    assert numbers["average_fee"] == round(numbers["mrr"] / max(1, numbers["active"]), 2)


def test_the_churn_is_a_share_of_the_running_subscriptions(subscriptions):
    numbers = summary(subscriptions)
    assert 0 <= numbers["churn_rate"] <= 1
    churned = int((subscriptions["churn_month"] == CURRENT_MONTH).sum())
    # The churn is a share of the subscriptions that were running at the
    # start of the month.
    running_before = len(active_in(subscriptions, MONTHS[MONTHS.index(CURRENT_MONTH) - 1]))
    assert numbers["churn_rate"] == round(churned / max(1, running_before), 4)


def test_the_new_mrr_is_the_revenue_of_the_new_subscriptions(subscriptions):
    numbers = summary(subscriptions)
    new = subscriptions[subscriptions["start_month"] == CURRENT_MONTH]
    assert numbers["new_mrr"] == round(float(new["monthly_fee"].sum()), 2)


def test_the_net_revenue_retention_is_a_share(subscriptions):
    numbers = summary(subscriptions)
    assert numbers["net_revenue_retention"] >= 0


def test_the_mrr_of_every_month_is_a_row_per_month(subscriptions):
    monthly = mrr_by_month(subscriptions)
    assert len(monthly) == len(MONTHS)
    assert list(monthly["month"]) == MONTHS
    assert (monthly["mrr"] >= 0).all()


def test_the_mrr_grows_when_a_customer_joins(subscriptions):
    monthly = mrr_by_month(subscriptions)
    assert monthly.iloc[0]["mrr"] <= monthly.iloc[-1]["mrr"]


def test_the_cohort_table_has_a_row_per_cohort(subscriptions):
    cohorts = cohort_retention(subscriptions)
    assert not cohorts.empty
    assert "cohort" in cohorts.columns
    for _, row in cohorts.iterrows():
        for month in MONTHS:
            value = row[month]
            if value is None or pd.isna(value):
                continue
            assert 0 <= value <= 1


def test_the_filters_narrow_the_data(subscriptions):
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

This lesson ties its explanation to `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### src/pipeline.py

### src/pipeline.py

```text
"""Subscription data and the metrics that are worked out from it.

The metrics are defined here, so the numbers on the page mean the same thing
everywhere:

MRR          the monthly fee of the subscriptions that are running in the
             month. It is the sum of the fee of every subscription that has
             started and has not churned yet.
ARR          the MRR of the current month times twelve.
Active       the subscriptions that are running in the current month.
Average fee  the MRR of the month divided by the number of active
             subscriptions (the revenue per customer).
Churn        the subscriptions that ended in the month, as a share of the
             subscriptions that were running at the start of the month.
New MRR      the MRR the new subscriptions of the month brought in.
Expansion    the extra MRR the subscriptions that were already there
             brought in.
Net revenue  the MRR of the subscriptions that were there a year ago, plus
             what they brought since, as a share of what they brought then.
             It is the number that says whether the business grows with the
             customers it already has.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

SEGMENTS = ["student", "starter", "team", "business"]
REGIONS = ["north", "south", "east", "west"]

#: The fee of a plan, before the discount every customer gets.
PLAN_FEE = {"student": 5, "starter": 12, "team": 29, "business": 79}

#: The months the data covers.
MONTHS = ["2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04"]

#: The month the page is about.
CURRENT_MONTH = "2026-04"


def _month_index(month: str) -> int:
    return MONTHS.index(month)


def make_subscriptions(count=180, seed=21, churn_rate=0.12):
    """A set of subscriptions with a start month and, for some of them, the
    month they churned in."""
    rng = np.random.default_rng(seed)
    plans = rng.choice(SEGMENTS, count, p=[0.3, 0.3, 0.25, 0.15])
    starts = rng.choice(MONTHS[:4], count, p=[0.3, 0.3, 0.2, 0.2])
    fees = np.array([PLAN_FEE[plan] for plan in plans]) * rng.uniform(0.9, 1.2, count)

    frame = pd.DataFrame({
        "customer_id": np.arange(1, count + 1),
        "segment": plans,
        "region": rng.choice(REGIONS, count),
        "start_month": starts,
        "monthly_fee": fees.round(2),
    })

    churned = []
    for start in frame["start_month"]:
        first = _month_index(start)
        room = len(MONTHS) - 1 - first
        if room > 0 and rng.random() < churn_rate:
            churned.append(MONTHS[first + int(rng.integers(1, room + 1))])
        else:
            churned.append(None)
    frame["churn_month"] = churned
    return frame


def is_active(row, month: str) -> bool:
    """True when a subscription is running in a month."""
    if _month_index(row["start_month"]) > _month_index(month):
        return False
    churn = row.get("churn_month")
    if churn is None or (isinstance(churn, float) and np.isnan(churn)):
        return True
    return _month_index(churn) > _month_index(month)


def active_in(frame: pd.DataFrame, month: str) -> pd.DataFrame:
    """The subscriptions that are running in a month."""
    if frame.empty:
        return frame
    mask = frame.apply(lambda row: is_active(row, month), axis=1)
    return frame[mask]


def mrr_by_month(frame: pd.DataFrame, months=None) -> pd.DataFrame:
    """The MRR of every month."""
    months = months or MONTHS
    rows = []
    for month in months:
        active = active_in(frame, month)
        rows.append({
            "month": month,
            "mrr": round(float(active["monthly_fee"].sum()), 2),
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
