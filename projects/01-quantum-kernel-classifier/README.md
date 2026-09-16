# 01 — Quantum Kernel Classifier

## Objective

Study a quantum-kernel workflow on a small nonlinear binary classification problem and compare it with classical kernel learning.

## Research questions

- How does a quantum feature map change the induced similarity structure?
- How does a quantum-kernel classifier compare with an RBF SVM under the same split?
- How sensitive are results to feature-map depth and data scaling?

## Method

1. Generate a deterministic two-feature dataset.
2. Standardize the features.
3. Build a parameterized quantum feature map.
4. Compute a quantum kernel matrix.
5. Train a classical SVM using the quantum kernel.
6. Compare with an RBF-SVM baseline.

## Scientific caution

This is a controlled research prototype. Small synthetic datasets cannot establish quantum advantage. Report test metrics, kernel-computation cost, circuit depth, and simulator/backend settings together.

## Suggested metrics

- Accuracy
- Balanced accuracy
- Precision
- Recall
- F1
- Kernel evaluation time
- Number of circuit evaluations

## Extension path

- FidelityQuantumKernel
- noise-aware kernel evaluation
- kernel alignment analysis
- multiple random seeds
- real datasets after the synthetic baseline is validated
