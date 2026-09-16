"""Classical baseline used to frame future QML experiments."""

from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def run_classical_baseline(random_state: int = 42) -> float:
    """Train a simple classical classifier and return held-out accuracy.

    This baseline is intentionally simple so future quantum models can be
    compared against a transparent reference under the same data split.
    """
    X, y = make_moons(n_samples=200, noise=0.15, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state, stratify=y
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(random_state=random_state))
    model.fit(X_train, y_train)
    return float(model.score(X_test, y_test))


if __name__ == "__main__":
    print(f"Classical baseline accuracy: {run_classical_baseline():.4f}")
