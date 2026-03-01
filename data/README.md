# Dataset

This project is designed for multimodal PTSD detection using speech and text signals.

Typical datasets used in PTSD research include:

- DAIC-WOZ (Distress Analysis Interview Corpus)
- Other clinical interview datasets with speech recordings and transcripts

Dataset link (example):

https://dcapswoz.ict.usc.edu/

## Data Structure

After obtaining the dataset, place files in the following structure:

data/

    audio/

        *.wav

    transcripts/

        *.txt

    metadata/

        labels.csv

## Modalities

The project supports the following modalities:

Audio features:
- MFCC
- Pitch
- Energy
- Speaking rate

Text features:
- TF-IDF
- Transformer embeddings

Optional behavioral signals:
- Eye-tracking
- Session metadata

## Note

Due to privacy and licensing restrictions, raw data cannot be distributed in this repository.

Researchers should request access through the official dataset providers.
# Data (Not Included)

Raw datasets are **not included in this repository** due to licensing, privacy, and data-use restrictions.

This project was developed using publicly available behavioral health datasets such as:

- **DAIC-WOZ** (Distress Analysis Interview Corpus – Wizard of Oz)
- Audio recordings
- Speech transcripts
- Behavioral features (gaze, facial AUs, head pose)

These datasets contain sensitive participant information and must be obtained directly from the original data providers.

---

# How to Obtain the Data

You can request the dataset from the official source:

DAIC-WOZ dataset page  
https://dcapswoz.ict.usc.edu/

Follow their instructions to obtain the data.

---

# Expected Local Folder Structure

After downloading the dataset, store it **locally** (not in this repo).

Example:
