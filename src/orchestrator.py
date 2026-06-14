from __future__ import annotations

from typing import Dict

from agents import (
    ComplianceAgent,
    ContradictionAgent,
    EvidenceAgent,
    ReportAgent,
    RiskAgent,
    TimelineAgent,
)


class SupervisorAgent:
    name = "Supervisor Agent"

    def run(self, case_data: Dict[str, str]) -> Dict:
        evidence_agent = EvidenceAgent()
        timeline_agent = TimelineAgent()
        contradiction_agent = ContradictionAgent()
        compliance_agent = ComplianceAgent()
        risk_agent = RiskAgent()
        report_agent = ReportAgent()

        evidence_result = evidence_agent.run(case_data)
        timeline_result = timeline_agent.run(case_data)
        contradiction_result = contradiction_agent.run(case_data)
        compliance_result = compliance_agent.run(case_data)
        risk_result = risk_agent.run(
            contradictions=contradiction_result.output.get("contradictions", []),
            failed_checks=compliance_result.output.get("failed_checks", []),
        )
        report_result = report_agent.run(
            evidence=evidence_result.output,
            timeline=timeline_result.output,
            contradictions=contradiction_result.output,
            compliance=compliance_result.output,
            risk=risk_result.output,
        )

        supervisor_reasoning = [
            f"Processed {evidence_result.output.get('document_count', 0)} document(s).",
            f"Built a timeline with {len(timeline_result.output.get('timeline', []))} event(s).",
            f"Detected {contradiction_result.output.get('contradiction_count', 0)} contradiction(s).",
            f"Detected {len(compliance_result.output.get('failed_checks', []))} failed compliance control(s).",
            f"Assigned risk level {risk_result.output.get('risk_level', 'Unknown')} with score {risk_result.output.get('risk_score', 0)}/100.",
            f"Final recommendation: {report_result.output.get('recommendation', 'No recommendation')}.",
        ]

        return {
            "supervisor": self.name,
            "supervisor_reasoning": supervisor_reasoning,
            "evidence": evidence_result.output,
            "timeline": timeline_result.output,
            "contradictions": contradiction_result.output,
            "compliance": compliance_result.output,
            "risk": risk_result.output,
            "report": report_result.output,
        }


def analyze_case(case_data: Dict[str, str]) -> Dict:
    supervisor = SupervisorAgent()
    return supervisor.run(case_data)