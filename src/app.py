from __future__ import annotations

import streamlit as st

from orchestrator import analyze_case
from utils import read_case_files

st.set_page_config(page_title="Global CyberGuard Intelligence Hub", layout="wide")

st.title("Global CyberGuard Intelligence Hub")
st.caption("Multi-agent reasoning MVP for risk, compliance, and evidence analysis")

st.markdown("### Synthetic Case Input")

default_case = read_case_files()

col1, col2 = st.columns(2)

with col1:
    vendor_form = st.text_area(
        "Vendor Form",
        value=default_case.get("vendor_form", ""),
        height=180,
    )
    policy = st.text_area(
        "Policy",
        value=default_case.get("policy", ""),
        height=180,
    )
    incident_report = st.text_area(
        "Incident Report",
        value=default_case.get("incident_report", ""),
        height=180,
    )

with col2:
    activity_log = st.text_area(
        "Activity Log",
        value=default_case.get("activity_log", ""),
        height=180,
    )
    review_notes = st.text_area(
        "Review Notes",
        value=default_case.get("review_notes", ""),
        height=180,
    )

case_data = {
    "vendor_form": vendor_form,
    "policy": policy,
    "incident_report": incident_report,
    "activity_log": activity_log,
    "review_notes": review_notes,
}

if st.button("Analyze Case", use_container_width=True):
    results = analyze_case(case_data)

    st.markdown("---")
    st.subheader("Executive Summary")
    for line in results["report"]["summary"]:
        st.write(f"- {line}")

    st.subheader("Recommendation")
    st.success(results["report"]["recommendation"])

    st.subheader("Supervisor Reasoning")
    for step in results["supervisor_reasoning"]:
        st.write(f"- {step}")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Timeline")
        timeline_items = results["timeline"]["timeline"]
        if timeline_items:
            for item in timeline_items:
                st.write(f"- {item}")
        else:
            st.write("No timeline events found.")

        st.subheader("Contradictions")
        contradictions = results["contradictions"]["contradictions"]
        if contradictions:
            for item in contradictions:
                st.write(f"- {item}")
        else:
            st.write("No contradictions found.")

    with c2:
        st.subheader("Compliance Checks")
        failed_checks = results["compliance"]["failed_checks"]
        passed_checks = results["compliance"]["passed_checks"]

        if failed_checks:
            st.error("Failed Checks")
            for item in failed_checks:
                st.write(f"- {item}")

        if passed_checks:
            st.success("Passed Checks")
            for item in passed_checks:
                st.write(f"- {item}")

        if not failed_checks and not passed_checks:
            st.write("No compliance checks available.")

        st.subheader("Risk Assessment")
        st.metric("Risk Score", results["risk"]["risk_score"])
        st.write(f"**Risk Level:** {results['risk']['risk_level']}")
        for reason in results["risk"]["rationale"]:
            st.write(f"- {reason}")

    st.subheader("Extracted Evidence")
    evidence_facts = results["evidence"]["facts"]
    if evidence_facts:
        for fact in evidence_facts:
            st.write(f"- {fact}")
    else:
        st.write("No evidence extracted.")