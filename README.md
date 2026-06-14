# Global CyberGuard Intelligence Hub

## Overview
Global CyberGuard Intelligence Hub is a multi-agent reasoning system designed to analyze synthetic risk and compliance cases where evidence is fragmented across documents, logs, reports, and notes.

The system coordinates specialized agents to extract facts, build a timeline, detect contradictions, evaluate compliance, assess risk, and generate a final report.

## Hackathon Track
**Reasoning Agents**

## Microsoft IQ Layer
**Foundry IQ**  
The architecture is designed to use Foundry IQ as the grounding and enterprise knowledge layer for cited, context-aware retrieval.

## Problem
Complex cases are often reviewed manually across multiple disconnected sources. This creates delays, weak traceability, inconsistent decisions, and higher operational risk.

## Solution
A multi-agent workflow that:
- extracts evidence,
- organizes chronology,
- detects contradictions,
- checks policy alignment,
- scores risk,
- and produces a final recommendation.

## Agent Roles
- **Supervisor Agent**: coordinates the full workflow
- **Evidence Agent**: extracts relevant facts
- **Timeline Agent**: orders events chronologically
- **Contradiction Agent**: identifies conflicts across sources
- **Compliance Agent**: checks alignment with policy requirements
- **Risk Agent**: estimates severity level
- **Report Agent**: generates the final report

## Input Files
Synthetic case documents stored in `/data`:
- `vendor_form.md`
- `policy.md`
- `incident_report.md`
- `activity_log.md`
- `review_notes.md`

## Project Structure
```text
docs/
data/
src/
demo/
README.md
requirements.txt
.gitignore