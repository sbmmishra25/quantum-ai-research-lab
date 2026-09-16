"""Small VQC experiment compatible with current Qiskit Machine Learning APIs."""

from __future__ import annotations

import numpy as np
from qiskit.circuit.library import TwoLocal, zz_feature_map
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.optimizers import COBYLA


def make_vqc(num_features: int = 2, maxiter: int = 30) -> VQC:
    """Build a two-qubit variational quantum classifier."""
    if num_features < 1:
        raise ValueError("num_features must be positive")

    feature_map = zz_feature_map(num_features)
    ansatz = TwoLocal(
        num_qubits=num_features,
        rotation_blocks="ry",
        entanglement_blocks="cz",
        reps=1,
        entanglement="linear",
    )
    sampler = StatevectorSampler(seed=42)
    return VQC(
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=COBYLA(maxiter=maxiter),
        sampler=sampler,
    )


def run_vqc(random_state: int = 42, maxiter: int = 30) -> float:
    """Train a compact VQC on a deterministic synthetic binary dataset."""
    rng = np.random.default_rng(random_state)
    X = rng.uniform(-1.0, 1.0, size=(80, 2))
    y = (X[:, 0] * X[:, 1] > 0).astype(int)

    model = make_vqc(num_features=2, maxiter=maxiter)
    model.fit(X, y)
    return float(model.score(X, y))


if __name__ == "__main__":
    print(f"VQC training accuracy: {run_vqc():.4f}")
