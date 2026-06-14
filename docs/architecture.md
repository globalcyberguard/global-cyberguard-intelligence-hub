# Architecture

## Overview
Global CyberGuard Intelligence Hub is a multi-agent reasoning system designed to analyze synthetic cases involving fragmented evidence, policy checks, and risk signals.

## Core Components
- User Interface (Streamlit)
- Orchestrator
- Supervisor Agent
- Evidence Agent
- Timeline Agent
- Contradiction Agent
- Compliance Agent
- Risk Agent
- Report Agent
- Foundry IQ Knowledge Layer

## High-Level Flow
1. The user submits a synthetic case
2. The Orchestrator sends the case to the Supervisor Agent
3. The Evidence Agent extracts relevant facts
4. The Timeline Agent orders events chronologically
5. The Contradiction Agent identifies inconsistencies
6. The Compliance Agent checks policy alignment
7. The Risk Agent scores severity
8. The Report Agent generates the final report
9. The user receives a structured decision output

## Mermaid Diagram

```mermaid
flowchart TD
    A[User] --> B[Streamlit UI]
    B --> C[Orchestrator]
    C --> D[Supervisor Agent]
    D --> E[Evidence Agent]
    D --> F[Timeline Agent]
    D --> G[Contradiction Agent]
    D --> H[Compliance Agent]
    D --> I[Risk Agent]
    E --> J[Consolidated Analysis]
    F --> J
    G --> J
    H --> J
    I --> J
    J --> K[Report Agent]
    K --> L[Results Dashboard]
    D --> M[Foundry IQ Knowledge Layer]
    M --> J