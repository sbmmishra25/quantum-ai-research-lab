"""Classical baseline used for controlled QML comparisons."""

from __future__ import annotations

from time import perf_counter

from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def run_classical_baseline(random_state: int = 42) -> dict[str, float]:
    """Train a transparent classical baseline on the shared experiment split."""
    X, y = make_moons(n_samples=200, noise=0.15, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state, stratify=y
    )

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=random_state),
    )

    start = perf_counter()
    model.fit(X_train, y_train)
    runtime = perf_counter() - start
    predictions = model.predict(X_test)

    return {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "balanced_accuracy": float(balanced_accuracy_score(y_test, predictions)),
        "precision": float(precision_score(y_test, predictions, zero_division=0)),
        "recall": float(recall_score(y_test, predictions, zero_division=0)),
        "f1": float(f1_score(y_test, predictions, zero_division=0)),
        "runtime_seconds": float(runtime),
        "train_samples": float(len(X_train)),
        "test_samples": float(len(X_test)),
    }


if __name__ == "__main__":
    results = run_classical_baseline()
    for metric, value in results.items():
        print(f"{metric}: {value:.6f}")
