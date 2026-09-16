"""Evaluation helpers for reproducible QML experiments."""

from __future__ import annotations

from typing import Any

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)


def classification_metrics(y_true: Any, y_pred: Any) -> dict[str, float]:
    """Return a compact, reproducible set of binary-classification metrics."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }


def circuit_resources(circuit: Any) -> dict[str, int]:
    """Summarize basic circuit resources when a Qiskit circuit is supplied."""
    return {
        "num_qubits": int(circuit.num_qubits),
        "depth": int(circuit.depth() or 0),
        "size": int(circuit.size()),
        "parameters": int(circuit.num_parameters),
    }
