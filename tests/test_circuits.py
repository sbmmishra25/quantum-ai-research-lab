import unittest

from qiskit import QuantumCircuit

from src.quantum_ai.circuits import bell_state, feature_map


class TestCircuits(unittest.TestCase):
    def test_bell_state_shape(self):
        circuit = bell_state()
        self.assertIsInstance(circuit, QuantumCircuit)
        self.assertEqual(circuit.num_qubits, 2)
        self.assertEqual(circuit.num_clbits, 2)

    def test_feature_map_shape(self):
        circuit = feature_map(0.5)
        self.assertEqual(circuit.num_qubits, 1)
        self.assertEqual(circuit.num_clbits, 0)


if __name__ == "__main__":
    unittest.main()
