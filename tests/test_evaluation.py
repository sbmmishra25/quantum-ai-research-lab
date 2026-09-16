import unittest

from src.quantum_ai.evaluation import classification_metrics


class EvaluationTests(unittest.TestCase):
    def test_binary_metrics_are_reported(self):
        metrics = classification_metrics([0, 0, 1, 1], [0, 1, 1, 1])
        self.assertEqual(set(metrics), {
            "accuracy",
            "balanced_accuracy",
            "precision",
            "recall",
            "f1",
        })
        for value in metrics.values():
            self.assertGreaterEqual(value, 0.0)
            self.assertLessEqual(value, 1.0)


if __name__ == "__main__":
    unittest.main()
