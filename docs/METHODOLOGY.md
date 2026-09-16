# Experimental Methodology

## Objective

Evaluate quantum and hybrid quantum-classical approaches using transparent, reproducible experiments.

## Required experiment record

Each experiment should record:

- Problem definition
- Dataset or synthetic data generation method
- Preprocessing
- Classical baseline
- Quantum model or algorithm
- Circuit depth and qubit count
- Optimizer and hyperparameters
- Random seed
- Evaluation metrics
- Runtime/resource observations
- Noise assumptions or simulator configuration
- Limitations

## Benchmarking principle

A quantum model should not be described as superior merely because it achieves a favorable metric on one small dataset. Comparisons should consider accuracy or task performance together with training cost, inference cost, circuit depth, number of qubits, noise sensitivity, and reproducibility.

## Suggested evaluation

For classification tasks:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Calibration where appropriate

For optimization tasks:

- Objective value
- Constraint violations
- Approximation quality
- Runtime
- Number of function evaluations
- Sensitivity to noise and initialization

## Reproducibility checklist

- [ ] Fixed or recorded random seeds
- [ ] Environment/dependency versions recorded
- [ ] Dataset provenance documented
- [ ] Classical baseline included
- [ ] Hyperparameters recorded
- [ ] Circuit configuration recorded
- [ ] Evaluation protocol documented
- [ ] Limitations reported
