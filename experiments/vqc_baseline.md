# VQC Baseline Experiment

## Objective

Evaluate a compact Variational Quantum Classifier (VQC) on a deterministic two-feature binary classification problem and compare it with a transparent classical baseline.

## Dataset

The experiment generates 80 two-dimensional samples with a fixed random seed. The target is defined by the sign of the product of the two features, creating a nonlinear decision structure.

This synthetic dataset is intentionally small and should be treated as a research-development baseline, not evidence of quantum advantage.

## Quantum model

- Two qubits
- ZZ feature map
- TwoLocal ansatz
- RY rotation blocks
- CZ entanglement
- One repetition
- COBYLA optimizer
- StatevectorSampler with a fixed seed

The implementation follows the current Qiskit Machine Learning VQC interface and Qiskit 2.x-compatible primitive model.

## Evaluation

The first implementation reports training accuracy to keep the experiment simple. The next iteration should add a fixed train/test split, balanced accuracy, precision, recall, F1, optimization history, circuit depth, parameter count, and runtime.

## Research questions

1. How does the VQC compare with Logistic Regression on the same feature space?
2. How does ansatz depth affect performance and optimization stability?
3. How sensitive is the result to shot noise and initialization?
4. What changes under simulated device noise?
5. Does a quantum-kernel approach provide complementary behavior?

## Reproducibility

All stochastic components in the starter experiment use explicit seeds. Results should always be reported together with the dataset generation rule, train/test protocol, optimizer configuration, circuit structure, and simulator/backend settings.
