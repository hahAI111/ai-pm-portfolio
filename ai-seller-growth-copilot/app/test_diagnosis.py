import pathlib
import sys
import unittest

import pandas as pd

sys.path.append(str(pathlib.Path(__file__).parent))
from diagnosis import diagnose_seller, generate_action_plan, generate_seller_response


class GrowthCopilotTests(unittest.TestCase):
    def setUp(self):
        self.row = pd.read_csv(pathlib.Path(__file__).parent / "sample_seller_data.csv").iloc[0]

    def test_detects_conversion_as_primary_blocker(self):
        result = diagnose_seller(self.row)
        self.assertEqual(result["primary_blocker"], "Conversion issue")
        self.assertGreaterEqual(result["confidence"], 0.9)

    def test_generates_prioritized_actions(self):
        actions = generate_action_plan(self.row, diagnose_seller(self.row))
        self.assertEqual(actions[0]["priority"], "P0")
        self.assertGreaterEqual(len(actions), 3)

    def test_response_uses_diagnosis(self):
        response = generate_seller_response(self.row, diagnose_seller(self.row), "Why did sales decline?")
        self.assertIn("conversion issue", response.lower())


if __name__ == "__main__":
    unittest.main()
