# Global CyberGuard Intelligence Hub

## Overview

Global CyberGuard Intelligence Hub is a multi-agent reasoning system designed to support the analysis of complex risk and compliance cases where critical information is distributed across documents, activity logs, reports, review notes, and policy references.

The platform coordinates a set of specialized agents that work together to transform fragmented evidence into a structured analytical workflow. Instead of treating a case as a single document review, the system approaches it as a reasoning process: extracting relevant facts, reconstructing the sequence of events, identifying inconsistencies across sources, evaluating alignment with policy requirements, estimating risk severity, and generating a final recommendation.

## Hackathon Track

**Reasoning Agents**

## Microsoft IQ Layer

**Foundry IQ**

The architecture is aligned with Foundry IQ as the grounding knowledge layer, strengthening contextual analysis and supporting more reliable outputs within a structured multi-agent design.

## Problem

In many operational environments, complex cases still depend on manual review across disconnected sources. When evidence is fragmented, analysis becomes slower, less consistent, and harder to trace. This affects decision quality, increases review effort, and makes it more difficult to identify contradictions, policy breaches, and risk exposure in time.

## Solution

Global CyberGuard Intelligence Hub addresses this challenge through a coordinated multi-agent workflow that:

* extracts relevant facts from multiple inputs
* organizes chronology into a clear sequence of events
* detects contradictions and inconsistencies across sources
* evaluates alignment with policy requirements
* scores risk severity based on the findings
* consolidates the analysis into a final recommendation

## Agent Roles

* **Supervisor Agent**: coordinates the full analytical workflow and consolidates results
* **Evidence Agent**: extracts relevant facts from the source materials
* **Timeline Agent**: reconstructs the sequence of events chronologically
* **Contradiction Agent**: identifies inconsistencies across documents and records
* **Compliance Agent**: evaluates alignment with policy requirements
* **Risk Agent**: estimates severity level based on detected issues
* **Report Agent**: generates the final report and recommendation

## Input Files

Example case documents stored in `/data`:

* `vendor_form.md`
* `policy.md`
* `incident_report.md`
* `activity_log.md`
* `review_notes.md`

## Project Structure

```text
docs/
data/
src/
demo/
README.md
requirements.txt
.gitignore
```

## Run Locally

```bash
cd src
python -m streamlit run app.py
```

## Expected Output

The application returns:

* executive summary
* recommendation
* supervisor reasoning
* timeline
* contradictions
* compliance findings
* risk score
* extracted evidence

## Architecture

The system uses a multi-agent orchestration pattern:

1. The user submits a case
2. The Orchestrator passes the case to the Supervisor Agent
3. The Evidence Agent extracts relevant facts
4. The Timeline Agent orders events chronologically
5. The Contradiction Agent identifies inconsistencies
6. The Compliance Agent checks policy alignment
7. The Risk Agent scores severity
8. The Report Agent generates the final report

Foundry IQ is represented as the grounding knowledge layer in the architecture design.

## Architecture Diagram

![Architecture Diagram](demo/architecture-diagram.png)

## Repository Compliance

This public repository is structured to exclude:

* secrets
* API keys
* tokens
* personally identifiable information
* internal proprietary information
* restricted or private materials

## Screenshots

### Input Screen

![Input Screen](demo/01-input-screen.png)

### Results Summary

![Results Summary](demo/02-results-summary.png)

### Results Details

![Results Details](demo/03-results-details.png)

## Demo Goal

Demonstrate how a multi-agent reasoning system can support faster, more structured, and more reliable case analysis in risk and compliance workflows.

## Notes

This MVP focuses on transparent reasoning, structured analysis, and explainable outputs within a public-facing hackathon submission.
