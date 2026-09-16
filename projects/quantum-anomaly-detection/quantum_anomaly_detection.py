"""Quantum-kernel anomaly detection with a one-class SVM.

Normal training data define the reference distribution. A quantum kernel is
used to create a precomputed similarity matrix for OneClassSVM. A classical
RBF OneClassSVM is evaluated on the same split for comparison.
"""

from __future__ import annotations

import numpy as np
from qiskit.circuit.library import zz_feature_map
from qiskit_machine_learning.kernels import FidelityStatevectorKernel
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM


def make_anomaly_data(seed: int = 42):
    rng = np.random.default_rng(seed)
    train_normal = rng.normal(loc=0.0, scale=0.55, size=(50, 2))
    test_normal = rng.normal(loc=0.0, scale=0.55, size=(25, 2))
    test_anomaly = rng.normal(loc=2.4, scale=0.35, size=(12, 2))

    X_test = np.vstack([test_normal, test_anomaly])
    y_test = np.concatenate([np.zeros(len(test_normal)), np.ones(len(test_anomaly))])

    scaler = MinMaxScaler(feature_range=(0.0, np.pi))
    scaler.fit(np.vstack([train_normal, X_test]))
    return scaler.transform(train_normal), scaler.transform(X_test), y_test


def _to_anomaly_labels(one_class_predictions):
    return (np.asarray(one_class_predictions) == -1).astype(int)


def evaluate(seed: int = 42) -> dict[str, dict[str, float]]:
    X_train, X_test, y_test = make_anomaly_data(seed)

    classical = OneClassSVM(kernel="rbf", gamma="scale", nu=0.15)
    classical.fit(X_train)
    classical_pred = _to_anomaly_labels(classical.predict(X_test))

    feature_map = zz_feature_map(feature_dimension=2, reps=2)
    qkernel = FidelityStatevectorKernel(feature_map=feature_map)
    K_train = qkernel.evaluate(X_train)
    K_test = qkernel.evaluate(X_test, X_train)

    quantum = OneClassSVM(kernel="precomputed", nu=0.15)
    quantum.fit(K_train)
    quantum_pred = _to_anomaly_labels(quantum.predict(K_test))

    def metrics(pred):
        return {
            "precision": float(precision_score(y_test, pred, zero_division=0)),
            "recall": float(recall_score(y_test, pred, zero_division=0)),
            "f1": float(f1_score(y_test, pred, zero_division=0)),
        }

    return {
        "classical_rbf_one_class_svm": metrics(classical_pred),
        "quantum_kernel_one_class_svm": metrics(quantum_pred),
    }


if __name__ == "__main__":
    print(evaluate())
