from schema import ResultCard, SourceItem


DEFAULT_RESULTS = [
    ResultCard(
        title="Validated report – Distal radius fracture (Colles)",
        relevance_score=93,
        findings="Transverse distal radius fracture with mild dorsal displacement.",
        impression="Consistent with Colles' fracture.",
        tags=["SNOMED:263204007", "RadGraph✓", "NLI entailment"],
        sources=[
            SourceItem(label="MIMIC-CXR study #A123", kind="PhysioNet"),
            SourceItem(label="CheXpert Guidelines (Stanford)", kind="Guideline"),
            SourceItem(label="SNOMED CT 263204007", kind="SNOMED"),
        ],
    ),
    ResultCard(
        title="Similar case – Forearm fracture teaching file",
        relevance_score=88,
        findings="Teaching case with imaging-report alignment for distal radius injury.",
        impression="Related case supporting distal radius fracture interpretation.",
        tags=["PACS", "TeachingFile"],
        sources=[
            SourceItem(label="MIMIC-CXR study #A123", kind="PhysioNet"),
            SourceItem(label="CheXpert Guidelines (Stanford)", kind="Guideline"),
        ],
    ),
]


ALTERNATE_RESULTS = [
    ResultCard(
        title="Validated report – Metacarpal shaft fracture",
        relevance_score=91,
        findings="Oblique fracture line through the metacarpal shaft without major angulation.",
        impression="Findings favor a non-comminuted metacarpal fracture.",
        tags=["SNOMED:43422006", "RadGraph✓", "NLI entailment"],
        sources=[
            SourceItem(label="Orthopedic teaching file #M77", kind="TeachingFile"),
            SourceItem(label="Emergency imaging guideline", kind="Guideline"),
        ],
    ),
    ResultCard(
        title="Reference note – Hand trauma pattern library",
        relevance_score=84,
        findings="Indexed hand-trauma reference with ontology-linked fracture labels.",
        impression="Supportive evidence for trauma education use case.",
        tags=["PACS", "Ontology-linked"],
        sources=[
            SourceItem(label="Institutional PACS sample", kind="PACS"),
            SourceItem(label="SNOMED CT fracture branch", kind="SNOMED"),
        ],
    ),
]
