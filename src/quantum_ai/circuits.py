"""Small, dependency-light quantum circuit utilities for research baselines."""

from qiskit import QuantumCircuit


def bell_state() -> QuantumCircuit:
    """Return a two-qubit Bell-state preparation circuit."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def feature_map(angle: float) -> QuantumCircuit:
    """Encode one scalar feature into a one-qubit rotation circuit."""
    circuit = QuantumCircuit(1)
    circuit.ry(angle, 0)
    return circuit
