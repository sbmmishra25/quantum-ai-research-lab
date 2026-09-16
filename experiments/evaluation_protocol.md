# Evaluation Protocol

## Goal

Compare quantum and classical classifiers under the same data generation rule, train/test split, and reporting conventions.

## Dataset protocol

- Synthetic two-dimensional nonlinear binary classification task
- 200 total samples
- Noise: 0.15
- Fixed random seed: 42
- Stratified 75/25 train/test split

## Required metrics

Report at minimum:

- Accuracy
- Balanced accuracy
- Precision
- Recall
- F1 score
- Runtime

For quantum models also report:

- Number of qubits
- Circuit depth
- Circuit size
- Trainable parameter count
- Simulator/backend configuration
- Number of shots when sampling is used
- Optimizer and maximum iterations
- Random seeds

## Experimental controls

Quantum and classical models must use the same training and test partitions. Hyperparameter changes should be documented rather than selected from the test set.

## Statistical robustness

For future experiments, repeat the complete experiment over multiple random seeds and report mean, standard deviation, and confidence intervals where appropriate. A single small synthetic experiment must not be interpreted as evidence of quantum advantage.

## Noise study

The next phase should compare ideal statevector execution with shot-based sampling and simulated device noise. Noise-model assumptions and backend configuration must be recorded with every result.

## Research reporting

Results should distinguish:

1. predictive performance,
2. computational cost,
3. circuit/resource requirements,
4. robustness to noise and initialization,
5. limitations of the experimental setup.
