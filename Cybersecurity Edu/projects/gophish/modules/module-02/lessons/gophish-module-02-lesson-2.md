# Read api impl and campaign in the source

**Lesson ID:** `gophish-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py] and [campaign.go]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, NewCampaign, token, Plan, mark, RecordOpen, RecordClick, RecordReport, Summary; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, `campaign.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import secrets` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _sources() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _build_helper() -> Path | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _run_helper(campaigns: list) -> dict | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _fallback(campaigns: list) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _campaigns() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `campaign.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `campaign.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func NewCampaign(name, template string) *Campaign {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func token() string {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Plan(campaign *Campaign, targets []string) []Send {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func mark(campaign *Campaign, id string, field func(*Send)) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func RecordOpen(campaign *Campaign, id string) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func RecordClick(campaign *Campaign, id string) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/api_impl.py

```text
"""The API of the campaign planner: the sends, the events and the funnel.

The numbers come from the Go code of the project. A helper program is built
from the sources of the project (campaign.go, main.go and go.mod) with a
`main` that makes a Campaign with NewCampaign, plans the sends with Plan,
records the opens, the clicks and the reports with RecordOpen, RecordClick
and RecordReport and computes the funnel with Summary. No mail is sent: the
project simulates the delivery, so the events of the campaigns of the console
are recorded by the helper the same way the demo of main.go records them.
When the Go toolchain is not installed, the same code is mirrored in Python.
"""

from __future__ import annotations

import hashlib
import json
import secrets
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(tempfile.gettempdir()) / "foundev-go-helpers"
GO = shutil.which("go")

#: How long an answer of the helper is reused.
TTL = 30.0

#: The helper program: it plans the campaigns and prints them as JSON.
HELPER = r'''
package main

import (
	"encoding/json"
	"os"
)

func main() {
	var input struct {
		Campaigns []struct {
			Name     string `json:"name"`
			Template string `json:"template"`
			Targets  []string `json:"targets"`
			Opened   []int   `json:"opened"`
			Clicked  []int   `json:"clicked"`
			Reported []int   `json:"reported"`
		} `json:"campaigns"`
	}
	_ = json.NewDecoder(os.Stdin).Decode(&input)

	campaigns := []map[string]any{}
	for _, item := range input.Campaigns {
		campaign := NewCampaign(item.Name, item.Template)
		plan := Plan(campaign, item.Targets)
		for _, index := range item.Opened {
			if index >= 0 && index < len(plan) {
				RecordOpen(campaign, plan[index].TrackingID)
			}
		}
		for _, index := range item.Clicked {
			if index >= 0 && index < len(plan) {
				RecordClick(campaign, plan[index].TrackingID)
			}
		}
		for _, index := range item.Reported {
			if index >= 0 && index < len(plan) {
				RecordReport(campaign, plan[index].TrackingID)
			}
		}
		// the sends of the campaign, in the order of the plan, with the
		// events that were recorded on them
		sends := []Send{}
		for _, send := range plan {
			if current, ok := campaign.Sends[send.TrackingID]; ok {
				sends = append(sends, *current)
			}
		}
		campaigns = append(campaigns, map[string]any{
			"name":     campaign.Name,
			"template": campaign.Template,
			"plan":     sends,
			"summary":  Summary(campaign),
		})
	}

	encoder := json.NewEncoder(os.Stdout)
	encoder.SetIndent("", "  ")
	_ = encoder.Encode(map[string]any{"campaigns": campaigns})
}
'''

#: The campaigns of the console. The events are recorded, no mail is sent.
CAMPAIGNS = [
    {
        "name": "Q3 awareness",
        "template": "password-reset",
        "targets": [
```

### campaign.go

```text
package main

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"strings"
	"time"
)

// Target is one recipient in an awareness campaign.
type Target struct {
	Email string `json:"email"`
	Name  string `json:"name"`
}

// Send records one simulated delivery.
type Send struct {
	TrackingID string    `json:"tracking_id"`
	Email      string    `json:"email"`
	SentAt     time.Time `json:"sent_at"`
	Opened     bool      `json:"opened"`
	Clicked    bool      `json:"clicked"`
	Reported   bool      `json:"reported"`
}

// Campaign groups sends under one name and template.
type Campaign struct {
	Name     string           `json:"name"`
	Template string           `json:"template"`
	Sends    map[string]*Send `json:"sends"`
}

// Stats holds the funnel rates.
type Stats struct {
	Campaign   string  `json:"campaign"`
	Sent       int     `json:"sent"`
	Opened     int     `json:"opened"`
	Clicked    int     `json:"clicked"`
	Reported   int     `json:"reported"`
	OpenRate   float64 `json:"open_rate"`
	ClickRate  float64 `json:"click_rate"`
	ReportRate float64 `json:"report_rate"`
}

func NewCampaign(name, template string) *Campaign {
	return &Campaign{Name: name, Template: template, Sends: map[string]*Send{}}
}

// counter makes the fallback tokens unique.
var counter int64

// token returns the tracking id of a send.
//
// When the random source does not work the token still has to be unique, or
// two sends would share one tracking id and the first one would overwrite
// the second one in the map.
func token() string {
	buffer := make([]byte, 8)
	if _, err := rand.Read(buffer); err != nil {
		counter++
		return fmt.Sprintf("fallback-%d-%d", time.Now().UnixNano(), counter)
	}
	return hex.EncodeToString(buffer)
}

// Plan creates a send record for every non-empty target.
func Plan(campaign *Campaign, targets []string) []Send {
	plan := []Send{}
	for _, raw := range targets {
		email := strings.TrimSpace(raw)
		if email == "" {
			continue
		}
		send := Send{TrackingID: token(), Email: email, SentAt: time.Now().UTC()}
		campaign.Sends[send.TrackingID] = &send
		plan = append(plan, send)
	}
	return plan
}

func mark(campaign *Campaign, id string, field func(*Send)) bool {
	send, ok := campaign.Sends[id]
	if !ok {
		return false
	}
	field(send)
	return true
}

func RecordOpen(campaign *Campaign, id string) bool {
	return mark(campaign, id, func(send *Send) { send.Opened = true })
}

func RecordClick(campaign *Campaign, id string) bool {
	return mark(campaign, id, func(send *Send) { send.Opened = true; send.Clicked = true })
}

func RecordReport(campaign *Campaign, id string) bool {
	return mark(campaign, id, func(send *Send) { send.Reported = true })
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

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change. These security projects are dual-use: scan, intercept, phish, or operate honeypots only on systems you own or have explicit authorization to test. Keep intentionally vulnerable apps and security labs isolated, and use synthetic targets and credentials.

## Summary

This lesson ties its explanation to `web/api_impl.py`, `campaign.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
