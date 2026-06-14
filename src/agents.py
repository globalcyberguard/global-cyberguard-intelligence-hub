from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class AgentResult:
    agent: str
    output: Dict


class EvidenceAgent:
    name = "Evidence Agent"

    def run(self, case_data: Dict[str, str]) -> AgentResult:
        extracted_facts: List[str] = []

        vendor_form = case_data.get("vendor_form", "")
        policy = case_data.get("policy", "")
        incident_report = case_data.get("incident_report", "")
        activity_log = case_data.get("activity_log", "")
        review_notes = case_data.get("review_notes", "")

        for source_name, content in [
            ("vendor_form", vendor_form),
            ("policy", policy),
            ("incident_report", incident_report),
            ("activity_log", activity_log),
            ("review_notes", review_notes),
        ]:
            lines = [line.strip() for line in content.splitlines() if line.strip()]
            for line in lines:
                extracted_facts.append(f"[{source_name}] {line}")

        return AgentResult(
            agent=self.name,
            output={
                "facts": extracted_facts,
                "document_count": len([v for v in case_data.values() if v.strip()]),
            },
        )


class TimelineAgent:
    name = "Timeline Agent"

    def run(self, case_data: Dict[str, str]) -> AgentResult:
        activity_log = case_data.get("activity_log", "")
        timeline: List[str] = []

        for line in activity_log.splitlines():
            line = line.strip()
            if line and line[0:4].isdigit():
                timeline.append(line)

        return AgentResult(
            agent=self.name,
            output={
                "timeline": timeline,
            },
        )


class ContradictionAgent:
    name = "Contradiction Agent"

    def run(self, case_data: Dict[str, str]) -> AgentResult:
        contradictions: List[str] = []

        vendor_form = case_data.get("vendor_form", "").lower()
        policy = case_data.get("policy", "").lower()
        incident_report = case_data.get("incident_report", "").lower()
        activity_log = case_data.get("activity_log", "").lower()
        review_notes = case_data.get("review_notes", "").lower()

        restricted_access_keywords = ["financial reporting dashboard", "restricted dashboard"]
        approval_missing_keywords = ["no manager approval found", "approval evidence is missing"]
        compliance_missing_keywords = ["compliance validation not recorded", "compliance review"]
        contract_missing_keywords = ["supporting contract file is missing", "valid contract verification"]

        if any(k in vendor_form for k in restricted_access_keywords):
            if "manager approval" in policy and any(k in activity_log for k in approval_missing_keywords):
                contradictions.append(
                    "The vendor requested access to a restricted system, but manager approval was not found."
                )

        if any(k in review_notes for k in contract_missing_keywords):
            contradictions.append(
                "The review notes indicate the contract evidence is missing, while policy requires contract verification."
            )

        if "compliance review" in policy and any(k in review_notes for k in compliance_missing_keywords):
            contradictions.append(
                "The policy requires compliance review, but review notes show no compliance validation was recorded."
            )

        if "alert" in incident_report and "policy mismatch" in activity_log:
            contradictions.append(
                "The incident report and activity log both indicate a policy mismatch tied to the onboarding request."
            )

        return AgentResult(
            agent=self.name,
            output={
                "contradictions": contradictions,
                "contradiction_count": len(contradictions),
            },
        )


class ComplianceAgent:
    name = "Compliance Agent"

    def run(self, case_data: Dict[str, str]) -> AgentResult:
        observations: List[str] = []
        passed_checks: List[str] = []
        failed_checks: List[str] = []

        policy = case_data.get("policy", "").lower()
        activity_log = case_data.get("activity_log", "").lower()
        review_notes = case_data.get("review_notes", "").lower()

        if "manager approval" in policy:
            if "no manager approval found" in activity_log:
                failed_checks.append("Manager approval requirement failed.")
            else:
                passed_checks.append("Manager approval requirement satisfied.")

        if "compliance review" in policy:
            if "compliance validation not recorded" in review_notes:
                failed_checks.append("Compliance review requirement failed.")
            else:
                passed_checks.append("Compliance review requirement satisfied.")

        if "contract verification" in policy:
            if "supporting contract file is missing" in review_notes:
                failed_checks.append("Contract verification requirement failed.")
            else:
                passed_checks.append("Contract verification requirement satisfied.")

        if failed_checks:
            observations.append("The case does not satisfy all policy controls.")
        else:
            observations.append("The case satisfies the visible policy controls.")

        return AgentResult(
            agent=self.name,
            output={
                "observations": observations,
                "passed_checks": passed_checks,
                "failed_checks": failed_checks,
            },
        )


class RiskAgent:
    name = "Risk Agent"

    def run(self, contradictions: List[str], failed_checks: List[str]) -> AgentResult:
        score = 0

        score += len(contradictions) * 20
        score += len(failed_checks) * 20

        score = min(score, 100)

        if score >= 80:
            level = "High"
        elif score >= 50:
            level = "Medium"
        else:
            level = "Low"

        rationale = []
        if contradictions:
            rationale.append(f"{len(contradictions)} contradiction(s) detected.")
        if failed_checks:
            rationale.append(f"{len(failed_checks)} compliance control(s) failed.")
        if not rationale:
            rationale.append("No major contradictions or failed checks detected.")

        return AgentResult(
            agent=self.name,
            output={
                "risk_score": score,
                "risk_level": level,
                "rationale": rationale,
            },
        )


class ReportAgent:
    name = "Report Agent"

    def run(
        self,
        evidence: Dict,
        timeline: Dict,
        contradictions: Dict,
        compliance: Dict,
        risk: Dict,
    ) -> AgentResult:
        summary_lines = [
            "Executive Summary",
            "This synthetic case was analyzed through a multi-agent workflow.",
            f"Documents processed: {evidence.get('document_count', 0)}",
            f"Timeline events found: {len(timeline.get('timeline', []))}",
            f"Contradictions detected: {contradictions.get('contradiction_count', 0)}",
            f"Risk level: {risk.get('risk_level', 'Unknown')} ({risk.get('risk_score', 0)}/100)",
        ]

        recommendation = "Approve"
        if risk.get("risk_level") == "High":
            recommendation = "Escalate and block access until controls are completed"
        elif risk.get("risk_level") == "Medium":
            recommendation = "Escalate for manual review before approval"

        return AgentResult(
            agent=self.name,
            output={
                "summary": summary_lines,
                "recommendation": recommendation,
            },
        )