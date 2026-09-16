"""Quantum-kernel classification baseline using Qiskit Machine Learning.

This project compares a fidelity quantum kernel classifier with a classical
RBF-kernel SVM on the same deterministic train/test split. It is intended as a
research baseline, not as evidence of quantum advantage.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from qiskit.circuit.library import zz_feature_map
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import FidelityStatevectorKernel
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


@dataclass
class BenchmarkResult:
    model: str
    accuracy: float
    balanced_accuracy: float
    f1: float
    runtime_seconds: float


def make_dataset(random_state: int = 42):
    X, y = make_moons(n_samples=120, noise=0.18, random_state=random_state)
    X = MinMaxScaler(feature_range=(0.0, 3.141592653589793)).fit_transform(X)
    return train_test_split(
        X, y, test_size=0.30, random_state=random_state, stratify=y
    )


def _metrics(name: str, y_true, y_pred, runtime: float) -> BenchmarkResult:
    return BenchmarkResult(
        model=name,
        accuracy=float(accuracy_score(y_true, y_pred)),
        balanced_accuracy=float(balanced_accuracy_score(y_true, y_pred)),
        f1=float(f1_score(y_true, y_pred)),
        runtime_seconds=float(runtime),
    )


def run_benchmark(random_state: int = 42) -> list[BenchmarkResult]:
    X_train, X_test, y_train, y_test = make_dataset(random_state)

    classical = SVC(kernel="rbf", gamma="scale")
    start = perf_counter()
    classical.fit(X_train, y_train)
    classical_pred = classical.predict(X_test)
    classical_time = perf_counter() - start

    feature_map = zz_feature_map(feature_dimension=2, reps=2)
    quantum_kernel = FidelityStatevectorKernel(feature_map=feature_map)
    quantum = QSVC(quantum_kernel=quantum_kernel)
    start = perf_counter()
    quantum.fit(X_train, y_train)
    quantum_pred = quantum.predict(X_test)
    quantum_time = perf_counter() - start

    return [
        _metrics("Classical RBF SVC", y_test, classical_pred, classical_time),
        _metrics("Quantum Kernel QSVC", y_test, quantum_pred, quantum_time),
    ]


if __name__ == "__main__":
    for result in run_benchmark():
        print(result)
