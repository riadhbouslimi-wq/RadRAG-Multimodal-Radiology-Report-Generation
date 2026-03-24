# RadRAG: Multimodal Radiology Report Generation with Retrieval-Augmented Grounding

## Overview
RadRAG is a multimodal retrieval-augmented generation (RAG) framework designed for clinically grounded radiology report generation. The system integrates medical image understanding, clinical language modeling, ontology-based reasoning, and evidence retrieval to produce accurate, interpretable, and verifiable radiology reports.

Unlike conventional generative models that often suffer from hallucinations and limited clinical reliability, RadRAG enforces factual consistency through hybrid retrieval, ontology alignment (e.g., SNOMED CT), and natural language inference (NLI)-based validation.

---

## Key Contributions

- **Multimodal Fusion**: Joint modeling of radiographic images and clinical text.
- **Hybrid Retrieval**: Combination of vector-based and keyword-based retrieval for evidence grounding.
- **Ontology Alignment**: Integration of standardized medical concepts (SNOMED CT) for structured and reproducible outputs.
- **Factual Validation**: Use of NLI and RadGraph-based validation to reduce hallucinations.
- **Explainability**: Evidence-linked report generation with traceable reasoning.
- **Educational Support**: Designed as a pedagogical tool for radiology training.

---

## System Architecture

The RadRAG pipeline consists of three main stages:

1. **Offline Training**
   - Vision encoder for radiographic feature extraction
   - Clinical language model fine-tuning (e.g., ClinicalT5)
   - Knowledge graph construction (SNOMED, RadGraph)

2. **Knowledge Indexing**
   - Hybrid indexing (BM25 + dense embeddings)
   - Clinical case database integration (e.g., MIMIC-CXR)

3. **Online Inference**
   - Multimodal query processing (image + text)
   - Evidence retrieval and ranking
   - Report generation
   - Factual validation (NLI)
   - Final clinically validated output

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

---

## Repository Structure
backend/ # API and inference pipeline
frontend/ # User interface (RadRAG demo)
results/ # Evaluation plots and figures
scripts/ # Plot generation and utilities
docs/ # Screenshots and additional materials
