from __future__ import annotations

from pathlib import Path
from typing import Dict


def read_case_files() -> Dict[str, str]:
    base = Path(__file__).resolve().parent.parent / "data"

    files = {
        "vendor_form": base / "vendor_form.md",
        "policy": base / "policy.md",
        "incident_report": base / "incident_report.md",
        "activity_log": base / "activity_log.md",
        "review_notes": base / "review_notes.md",
    }

    case_data: Dict[str, str] = {}

    for key, path in files.items():
        if path.exists():
            case_data[key] = path.read_text(encoding="utf-8")
        else:
            case_data[key] = ""

    return case_data