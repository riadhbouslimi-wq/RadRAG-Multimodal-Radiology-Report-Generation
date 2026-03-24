# RadRAG: Multimodal Radiology Report Generation with Retrieval-Augmented Grounding

## Overview
RadRAG is a multimodal retrieval-augmented generation (RAG) framework designed for clinically grounded radiology report generation. The system integrates medical image understanding, clinical language modeling, ontology-based reasoning, and hybrid evidence retrieval to produce accurate, interpretable, and verifiable radiology reports.

Unlike conventional generative models that often suffer from hallucinations and limited clinical reliability, RadRAG enforces factual consistency through retrieval-based grounding, ontology alignment (e.g., SNOMED CT), and natural language inference (NLI)-based validation.

---

## Key Contributions

- **Multimodal Fusion**: Joint modeling of radiographic images and clinical text.
- **Hybrid Retrieval**: Combination of dense vector retrieval and keyword-based search (BM25).
- **Ontology Alignment**: Integration of standardized medical concepts (SNOMED CT) for structured and reproducible outputs.
- **Factual Validation**: Use of NLI and RadGraph-based validation to reduce hallucinations and contradictions.
- **Explainability**: Evidence-linked report generation with traceable reasoning and sources.
- **Educational Support**: Designed as a pedagogical tool for radiology training and interpretability.

---

## System Architecture

The RadRAG pipeline consists of three main stages:

### 1. Offline Training
- Vision encoder for radiographic feature extraction
- Clinical language model fine-tuning (e.g., ClinicalT5)
- Knowledge graph construction using SNOMED CT and RadGraph

### 2. Knowledge Indexing
- Hybrid indexing (BM25 + dense embeddings)
- Integration of clinical case databases (e.g., MIMIC-CXR)
- Ontology-aware indexing for concept grounding

### 3. Online Inference
- Multimodal query processing (image + text)
- Evidence retrieval and ranking
- Report generation
- Factual validation using NLI
- Generation of clinically validated and evidence-grounded reports

---

## Results

### Quantitative Evaluation
- Nonlinear convergence across BLEU, ROUGE, CIDEr, and F1 metrics
- Baseline comparison with existing models (e.g., R2Gen)
- Ablation study demonstrating the contribution of:
  - Retrieval module
  - NLI-based validation
  - Ontology grounding

### Qualitative Evaluation
- Clinical vignette analysis demonstrating:
  - Improved diagnostic accuracy
  - Reduction of hallucinated findings
  - Precise and standardized medical terminology

### Key Findings
- Significant improvement in clinical F1-score
- Reduced hallucination rate
- Improved interpretability and reproducibility
- Strong alignment between quantitative metrics and clinical reasoning

---

## Datasets

This work is evaluated on publicly available medical imaging datasets:

- MIMIC-CXR (requires credentialed access via PhysioNet)
- CheXpert (Stanford University dataset)
- MURA dataset (musculoskeletal radiographs)

Due to data usage agreements and privacy constraints, the datasets are not included in this repository. Please refer to the official sources for access.

---

## External Resources

- SNOMED CT (clinical ontology for concept grounding)
- RadGraph (clinical structure extraction)
- PhysioNet (data access platform)

Note: SNOMED CT is subject to licensing restrictions and is not distributed in this repository.

---

## Repository Structure
backend/ # API and inference pipeline
frontend/ # User interface (RadRAG demo)
results/ # Evaluation plots and figures
scripts/ # Plot generation and utilities
docs/ # Screenshots and additional materials


---

## Reproducibility

This repository provides a demonstrator implementation of the RadRAG framework, including:
- Modular pipeline design
- Evaluation scripts and visualization tools
- Literature-aligned performance benchmarks

Note: Some components (e.g., trained model weights and full datasets) are not publicly distributed due to licensing and privacy constraints.

---

## Applications

- Radiology report generation
- Clinical decision support
- Medical AI education and training
- Explainable AI in healthcare

---

## Disclaimer

This project is intended for research and educational purposes only. It is not designed for direct clinical deployment or medical decision-making.
