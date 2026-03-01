# multimodal-ptsd-detection
Multimodal machine learning for PTSD detection using speech + text (and optional behavioral signals). Focus on feature fusion and evaluation.
# multimodal-ptsd-detection

Multimodal machine learning pipeline for PTSD detection using speech and text (and optional behavioral signals).  
This repository focuses on multimodal feature extraction, fusion strategies, and evaluation.

---

## Project Goal

Build a reliable screening-oriented classifier that predicts PTSD-related risk from multimodal signals while supporting interpretability and robust evaluation.

This work investigates whether combining behavioral signals such as speech and language improves machine learning models for mental health risk detection.

---

## Modalities

### Primary modalities
- **Audio** (prosody + spectral features)
- **Text** (transcripts / ASR output → NLP features)

### Optional modalities (if available)
- Eye-tracking / gaze features
- Behavioral interaction features
- Metadata (age, sex, session conditions)

---

## Methods (High Level)

### Feature Extraction

**Audio features**
- MFCCs
- Pitch
- Energy
- Speaking rate
- Pause statistics

**Text features**
- TF-IDF
- Transformer embeddings
- Lexical richness markers
- Sentiment indicators

---

### Fusion Strategies

We explore several multimodal fusion approaches:

- **Early Fusion**  
  Concatenate all modality features into a single vector.

- **Late Fusion**  
  Train separate models per modality and combine predictions.

- **Learned Fusion**  
  Train a small neural network over modality embeddings.

---

## Evaluation

### Metrics

Primary evaluation metrics:

- Balanced Accuracy
- F1 Score
- ROC-AUC

### Validation Protocol

To ensure reliable evaluation:

- Stratified cross-validation
- Participant-level data splitting (prevents data leakage)

---

## Repository Structure

---

## Notes on Data Availability

Due to privacy and licensing restrictions, raw datasets are **not included** in this repository.

This repository provides:

- Data processing pipeline
- Feature extraction code
- Model training and evaluation framework

Researchers should obtain datasets independently from their official sources.

---

## Contact

GitHub:  
https://github.com/himadriut
