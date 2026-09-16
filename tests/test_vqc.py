import unittest

from src.quantum_ai.vqc import make_vqc


class TestVQC(unittest.TestCase):
    def test_vqc_has_two_qubits(self):
        model = make_vqc(num_features=2, maxiter=1)
        self.assertEqual(model.feature_map.num_qubits, 2)
        self.assertEqual(model.ansatz.num_qubits, 2)

    def test_invalid_feature_count(self):
        with self.assertRaises(ValueError):
            make_vqc(num_features=0)


if __name__ == "__main__":
    unittest.main()
