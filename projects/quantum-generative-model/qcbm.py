"""Small Quantum Circuit Born Machine (QCBM) research prototype.

The model learns a four-state target probability distribution using a two-qubit
parameterized circuit and statevector probabilities. The objective is Jensen-
Shannon divergence, optimized with COBYLA.
"""

from __future__ import annotations

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scipy.optimize import minimize


TARGET = np.array([0.45, 0.05, 0.05, 0.45], dtype=float)


def circuit(parameters: np.ndarray) -> QuantumCircuit:
    if len(parameters) != 6:
        raise ValueError("QCBM expects exactly six trainable parameters.")
    qc = QuantumCircuit(2)
    qc.ry(parameters[0], 0)
    qc.ry(parameters[1], 1)
    qc.cz(0, 1)
    qc.rz(parameters[2], 0)
    qc.rz(parameters[3], 1)
    qc.ry(parameters[4], 0)
    qc.ry(parameters[5], 1)
    return qc


def probabilities(parameters: np.ndarray) -> np.ndarray:
    state = Statevector.from_instruction(circuit(parameters))
    probs = np.abs(np.asarray(state.data)) ** 2
    return probs / probs.sum()


def jensen_shannon(p: np.ndarray, q: np.ndarray, eps: float = 1e-12) -> float:
    p = np.clip(p, eps, 1.0)
    q = np.clip(q, eps, 1.0)
    p = p / p.sum()
    q = q / q.sum()
    m = 0.5 * (p + q)
    kl_pm = np.sum(p * np.log(p / m))
    kl_qm = np.sum(q * np.log(q / m))
    return float(0.5 * (kl_pm + kl_qm))


def train(seed: int = 42, maxiter: int = 150) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    initial = rng.uniform(-np.pi, np.pi, size=6)

    def objective(theta):
        return jensen_shannon(TARGET, probabilities(theta))

    result = minimize(objective, initial, method="COBYLA", options={"maxiter": maxiter})
    learned = probabilities(result.x)
    return {
        "success": bool(result.success),
        "iterations": int(result.nfev),
        "loss": float(result.fun),
        "target_distribution": TARGET.tolist(),
        "learned_distribution": learned.tolist(),
        "parameters": np.asarray(result.x).tolist(),
    }


if __name__ == "__main__":
    print(train())
