# Read test code and implementation evidence in the source

**Lesson ID:** `gophish-module-03-lesson-2`

## Purpose and learning objectives

Read the test cases in campaign_test.go beside the implementation in campaign.go. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `campaign_test.go`, `campaign.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `campaign_test.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `campaign_test.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func TestEveryTargetGetsItsOwnTrackingId(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestAnEmptyTargetIsSkipped(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestTheFunnelIsCounted(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestTheRatesAreShares(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestAnUnknownTrackingIdIsRefused(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### campaign_test.go

```text
package main

import (
	"strings"
	"testing"
)

func TestEveryTargetGetsItsOwnTrackingId(t *testing.T) {
	campaign := NewCampaign("demo", "hello")
	plan := Plan(campaign, []string{"ann@example.test", "bob@example.test"})

	if len(plan) != 2 {
		t.Fatalf("expected two sends, got %d", len(plan))
	}
	if plan[0].TrackingID == plan[1].TrackingID {
		t.Fatal("two sends may not share a tracking id")
	}
	if len(campaign.Sends) != 2 {
		t.Fatalf("expected two sends in the campaign, got %d", len(campaign.Sends))
	}
}

func TestAnEmptyTargetIsSkipped(t *testing.T) {
	campaign := NewCampaign("demo", "hello")
	plan := Plan(campaign, []string{"", "   ", "ann@example.test"})

	if len(plan) != 1 {
		t.Fatalf("expected one send, got %d", len(plan))
	}
}

func TestTheFunnelIsCounted(t *testing.T) {
	campaign := NewCampaign("demo", "hello")
	plan := Plan(campaign, []string{"ann@example.test", "bob@example.test", "cat@example.test"})

	RecordOpen(campaign, plan[0].TrackingID)
	RecordClick(campaign, plan[1].TrackingID)
	RecordReport(campaign, plan[2].TrackingID)

	summary := Summary(campaign)
	if summary.Sent != 3 {
		t.Fatalf("unexpected number of sends %d", summary.Sent)
	}
	// A click means the mail was opened as well.
	if summary.Opened != 2 {
		t.Fatalf("unexpected number of opens %d", summary.Opened)
	}
	if summary.Clicked != 1 {
		t.Fatalf("unexpected number of clicks %d", summary.Clicked)
	}
	if summary.Reported != 1 {
		t.Fatalf("unexpected number of reports %d", summary.Reported)
	}
}

func TestTheRatesAreShares(t *testing.T) {
	campaign := NewCampaign("demo", "hello")
	plan := Plan(campaign, []string{"ann@example.test", "bob@example.test"})

	RecordOpen(campaign, plan[0].TrackingID)
	RecordClick(campaign, plan[1].TrackingID)

	summary := Summary(campaign)
	// The click means the second mail was opened as well.
	if summary.OpenRate != 1 {
		t.Fatalf("unexpected open rate %v", summary.OpenRate)
	}
	if summary.ClickRate != 0.5 {
		t.Fatalf("unexpected click rate %v", summary.ClickRate)
	}
	if summary.ReportRate != 0 {
		t.Fatalf("unexpected report rate %v", summary.ReportRate)
	}
}

func TestAnUnknownTrackingIdIsRefused(t *testing.T) {
	campaign := NewCampaign("demo", "hello")
	if RecordOpen(campaign, "nope") {
		t.Fatal("an unknown tracking id should be refused")
	}
	if !strings.HasPrefix(NewCampaign("demo", "x").Name, "demo") {
		t.Fatal("the campaign keeps its name")
	}
}

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

This lesson ties its explanation to `campaign_test.go`, `campaign.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
