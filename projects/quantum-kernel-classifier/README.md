# Project 1 — Quantum Kernel Classifier

## Goal

Build a reproducible classification benchmark that compares a **quantum fidelity kernel + QSVC** with a classical RBF-kernel SVM on exactly the same data split.

## Why it matters

Quantum kernels map classical inputs through parameterized quantum feature maps and use state similarity to construct kernel matrices. This project studies that mechanism without assuming that the quantum method is superior.

## Implementation

- Synthetic nonlinear two-class dataset
- Fixed random seed and stratified train/test split
- Feature scaling to an angle-friendly range
- Two-qubit ZZ feature map
- Fidelity statevector quantum kernel
- QSVC classifier
- Classical RBF SVC comparator
- Accuracy, balanced accuracy, F1 and runtime reporting

## Run

```bash
python projects/quantum-kernel-classifier/quantum_kernel_classifier.py
```

## Research extensions

1. Repeat across 10+ seeds and report mean ± standard deviation.
2. Compare different feature maps and circuit depths.
3. Add kernel-target alignment and kernel-matrix diagnostics.
4. Replace the statevector reference with finite-shot execution.
5. Add simulated hardware noise.
6. Evaluate real tabular datasets after careful preprocessing.
7. Compare QSVC, PegasosQSVC and classical SVM variants.

## Scientific caution

Performance on a small synthetic dataset is a development result only. A claim of quantum advantage would require a substantially stronger experimental design, resource accounting, competitive classical baselines, and evidence that survives repeated evaluation.
