# Project 3 — Quantum Circuit Born Machine

## Goal

Implement a compact **Quantum Circuit Born Machine (QCBM)** that learns a target discrete probability distribution using a parameterized quantum circuit.

## Architecture

```text
Random parameters
      ↓
RY rotations
      ↓
CZ entanglement
      ↓
RZ + RY trainable layers
      ↓
Statevector probabilities
      ↓
Jensen-Shannon divergence
      ↓
COBYLA optimization
```

The two-qubit prototype represents four basis states. Its target distribution deliberately concentrates probability on two states, creating a simple but nontrivial generative-learning objective.

## Run

```bash
python projects/quantum-generative-model/qcbm.py
```

The script reports optimization status, objective value, target distribution, learned distribution and final parameters.

## Why this project is useful

Unlike discriminative QML projects, a Born machine directly studies **generative distribution learning**. This creates a foundation for research on quantum generative AI without pretending that a two-qubit demonstration is comparable to modern large generative models.

## Research extensions

- Increase qubit count and circuit expressivity
- Finite-shot training
- Hardware/noise-aware training
- Alternative divergences and maximum mean discrepancy
- Dataset-driven discretized distributions
- Compare with classical probabilistic models
- Study trainability and barren plateaus
- Conditional QCBMs
- Hybrid quantum-classical generative pipelines

## Evaluation

Future experiments should report distribution divergence, convergence behavior, circuit resources, repeated-seed statistics and classical baseline comparisons.
