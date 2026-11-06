# Read documented goals mapped to implementation in the source

**Lesson ID:** `gophish-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors campaign.go, main.go, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `campaign.go`, `main.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `campaign.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `campaign.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func NewCampaign(name, template string) *Campaign {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func token() string {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Plan(campaign *Campaign, targets []string) []Send {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func mark(campaign *Campaign, id string, field func(*Send)) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func RecordOpen(campaign *Campaign, id string) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func RecordClick(campaign *Campaign, id string) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# GoPhish

Plan a phishing-awareness campaign and score the results.

> An open-source phishing simulation platform used to run authorised awareness campaigns and staff training.

## Overview

An original, self-contained implementation of the **GoPhish** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Campaign and target models with unique tracking IDs
- Simulated send, open, click and report events
- Per-campaign statistics and rates
- JSON export for a training report

## Stack

`Go`
The CSV stack is Go. This build stores campaigns in memory and simulates delivery, so no mail server, database or tracking web server is required.

## Run

```bash
go run . -targets ana@example.com,bo@example.com
go test ./...
```

## Structure

```text
gophish/
├── main.go                campaign CLI
├── campaign.go            campaign and funnel logic
├── campaign_test.go       unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

5 tests: the tracking ids, the empty targets, the funnel, the rates and the
unknown tracking id.

## Notes and limitations

- No email is actually sent; events are recorded manually or from the demo.
- The tracking IDs are random strings, not signed tokens.
- Data is not persisted between runs.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production service; the notes above list the missing pieces.

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

### main.go

```text
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	name := flag.String("campaign", "Q3 awareness", "campaign name")
	template := flag.String("template", "password-reset", "email template")
	targets := flag.String("targets", "ana@example.com,bo@example.com", "comma separated targets")
	flag.Parse()

	campaign := NewCampaign(*name, *template)
	plan := Plan(campaign, strings.Split(*targets, ","))
	// The demo records a plausible funnel: everyone receives, half opens,
	// one clicks and one reports the message.
	if len(plan) > 0 {
		RecordOpen(campaign, plan[0].TrackingID)
	}
	if len(plan) > 1 {
		RecordClick(campaign, plan[1].TrackingID)
		RecordReport(campaign, plan[1].TrackingID)
	}

	encoder := json.NewEncoder(os.Stdout)
	encoder.SetIndent("", "  ")
	if err := encoder.Encode(map[string]any{"plan": plan, "summary": Summary(campaign)}); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

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

This lesson ties its explanation to `README.md`, `campaign.go`, `main.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
