# Experiments

This directory is reserved for reproducible experiment specifications and result summaries.

## Experiment 001 — Classical reference baseline

**Problem:** Binary classification on a synthetic non-linear dataset.

**Purpose:** Establish a transparent classical reference before introducing a quantum model.

**Dataset:** `sklearn.datasets.make_moons`, generated deterministically with a recorded random seed.

**Model:** StandardScaler + Logistic Regression.

**Metrics:** Held-out accuracy. Future experiments should add precision, recall, F1, confusion matrix, runtime, and resource measurements where appropriate.

## Planned experiments

- Quantum feature-map classification
- Variational quantum classifier
- Quantum-kernel classification
- Noise sensitivity study
- Classical versus hybrid quantum-classical comparison
- Resource-aware benchmarking

Results should be added only after the experiment is actually executed and validated.
