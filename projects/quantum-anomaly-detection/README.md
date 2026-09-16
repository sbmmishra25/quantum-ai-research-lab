# Project 2 — Quantum Kernel Anomaly Detection

## Goal

Explore anomaly detection with a **quantum similarity kernel** while retaining a directly comparable classical one-class SVM baseline.

## Use cases

The experimental pattern is relevant to domains such as equipment monitoring, cybersecurity telemetry, quality control, and rare-event screening. The included data are synthetic; this repository does not claim deployment readiness for any high-stakes application.

## Method

1. Generate a compact two-dimensional normal-data distribution.
2. Generate held-out normal and anomalous samples.
3. Scale features into a quantum encoding range.
4. Construct a ZZ quantum feature map.
5. Compute train and test fidelity-kernel matrices.
6. Fit `OneClassSVM(kernel="precomputed")` on the quantum kernel.
7. Compare against a classical RBF OneClassSVM.
8. Report anomaly precision, recall and F1.

## Run

```bash
python projects/quantum-anomaly-detection/quantum_anomaly_detection.py
```

## Research extensions

- Multiple anomaly types and contamination rates
- Precision-recall curves and threshold calibration
- Finite-shot kernel estimation
- Noise sensitivity
- Kernel alignment analysis
- Industrial predictive-maintenance datasets
- Cybersecurity datasets with strict leakage controls
- Comparison with Isolation Forest, LOF, autoencoders and deep SVDD

## Research value

This project is designed to test a concrete question: whether a quantum-induced similarity representation changes anomaly separability under controlled conditions. Results should be interpreted alongside strong classical anomaly-detection baselines.
