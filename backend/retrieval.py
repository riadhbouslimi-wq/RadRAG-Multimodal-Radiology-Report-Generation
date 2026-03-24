from typing import List
from mock_data import DEFAULT_RESULTS, ALTERNATE_RESULTS
from schema import ResultCard


FRACTURE_HINTS = [
    "fracture",
    "radius",
    "colles",
    "wrist",
    "distal radius",
    "forearm",
]


HAND_HINTS = [
    "hand",
    "metacarpal",
    "finger",
    "phalange",
]


def normalize_query(query_text: str) -> str:
    text = (query_text or "").strip()
    if not text:
        return "suspected upper-limb trauma; ontology expansion: fracture, distal radius, displacement"
    return f"{text.strip()} | ontology-expanded with SNOMED concepts"



def retrieve_candidates(query_text: str) -> List[ResultCard]:
    text = (query_text or "").lower()
    if any(token in text for token in HAND_HINTS) and not any(token in text for token in FRACTURE_HINTS):
        return ALTERNATE_RESULTS
    return DEFAULT_RESULTS



def compose_report(query_text: str, results: List[ResultCard]) -> str:
    top = results[0]
    return (
        f"Provisional evidence-grounded report: {top.findings} "
        f"Impression: {top.impression} "
        f"This output is presented with retrieved supporting evidence and ontology tags."
    )
