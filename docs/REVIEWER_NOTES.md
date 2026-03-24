# Reviewer Notes

## What this repository demonstrates

This repository is meant to accompany the RadRAG manuscript with a transparent, easy-to-run prototype that mirrors the system flow:

- multimodal query input,
- query normalization,
- hybrid retrieval,
- ontology-aware tagging,
- evidence-backed report presentation,
- history tracking.

## What is mocked

The present demo uses deterministic mock retrieval outputs for simplicity and reproducibility. The following components are placeholders and should be replaced with your real research modules when needed:

- SNOMED entity linking,
- image encoder inference,
- BM25/vector/concept fusion,
- cross-encoder reranking,
- ClinicalT5 generation,
- NLI/RadGraph factual validation.

## Why this is still useful for reviewers

Even with mocked outputs, the repository clarifies the software design of the proposed system and makes the manuscript more credible by showing:

1. the intended end-user workflow,
2. the structure of the API,
3. the expected data contract between UI and inference engine,
4. how evidence, scores, and ontology labels are exposed.

## Recommended sentence in the paper

You may add a sentence such as:

> To improve transparency and reproducibility, we provide a public demonstrator repository exposing the RadRAG user interface and the modular inference API used for multimodal querying, hybrid retrieval, ontology grounding, evidence presentation, and validated report generation.
