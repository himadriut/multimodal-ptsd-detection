"""
Example end-to-end pipeline runner (skeleton).

This script shows the typical flow:
1) Locate DAIC-WOZ data locally (NOT in this repo)
2) Load split files (train/dev/test)
3) Load pre-extracted features (or call feature extraction)
4) Train baseline models
5) Save results to results/

Fill in the TODO sections with your project-specific functions.
"""

import os
from pathlib import Path
import pandas as pd

# -----------------------------
# CONFIG
# -----------------------------
# Change this to your local DAIC-WOZ directory (not tracked by git)
DAIC_WOZ_DIR = Path(os.environ.get("DAIC_WOZ_DIR", "/Users/<your-username>/DAIC_WOZ"))
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_SPLIT = DAIC_WOZ_DIR / "train_split_Depression_AVEC2017.csv"
DEV_SPLIT   = DAIC_WOZ_DIR / "dev_split_Depression_AVEC2017.csv"
TEST_SPLIT  = DAIC_WOZ_DIR / "test_split_Depression_AVEC2017.csv"

# Example output file
OUT_METRICS = RESULTS_DIR / "baseline_metrics.csv"


def load_splits():
    train_df = pd.read_csv(TRAIN_SPLIT)
    dev_df   = pd.read_csv(DEV_SPLIT)
    test_df  = pd.read_csv(TEST_SPLIT)
    return train_df, dev_df, test_df


def main():
    print("DAIC_WOZ_DIR:", DAIC_WOZ_DIR)
    assert DAIC_WOZ_DIR.exists(), "Set DAIC_WOZ_DIR or export DAIC_WOZ_DIR=/path/to/DAIC_WOZ"

    train_split, dev_split, test_split = load_splits()
    print("Splits loaded:", train_split.shape, dev_split.shape, test_split.shape)

    # -----------------------------
    # TODO: load your engineered feature table
    # e.g., full_segments.csv created from notebooks
    # -----------------------------
    # features_path = DAIC_WOZ_DIR / "full_segments.csv"
    # features = pd.read_csv(features_path)
    # print("Features:", features.shape)

    # -----------------------------
    # TODO: merge splits with features
    # -----------------------------
    # train = features.merge(train_split, left_on="participant_id", right_on="participant_ID", how="inner")
    # dev   = features.merge(dev_split,   left_on="participant_id", right_on="participant_ID", how="inner")
    # test  = features.merge(test_split,  left_on="participant_id", right_on="participant_ID", how="inner")

    # -----------------------------
    # TODO: modeling + evaluation
    # -----------------------------
    # from sklearn.linear_model import LogisticRegression
    # from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
    #
    # X_train, y_train = ...
    # X_dev, y_dev = ...
    #
    # clf = LogisticRegression(max_iter=2000, class_weight="balanced")
    # clf.fit(X_train, y_train)
    # probs = clf.predict_proba(X_dev)[:, 1]
    # preds = (probs >= 0.5).astype(int)
    #
    # metrics = {
    #     "model": ["logreg"],
    #     "f1": [f1_score(y_dev, preds, zero_division=0)],
    #     "auc": [roc_auc_score(y_dev, probs)],
    #     "acc": [accuracy_score(y_dev, preds)],
    # }
    # pd.DataFrame(metrics).to_csv(OUT_METRICS, index=False)
    # print("Saved:", OUT_METRICS)

    print("Pipeline skeleton ready. Fill in TODO blocks based on your notebooks.")


if __name__ == "__main__":
    main()
