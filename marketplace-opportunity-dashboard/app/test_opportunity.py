import pathlib
import sys
import unittest

import pandas as pd

sys.path.append(str(pathlib.Path(__file__).parent))
from opportunity import calculate_opportunity_scores, recommend_initiative


class OpportunityDashboardTests(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv(pathlib.Path(__file__).parent / "sample_marketplace_data.csv")
        self.scored = calculate_opportunity_scores(self.data)

    def test_scores_are_bounded(self):
        self.assertTrue(self.scored["opportunity_score"].between(0, 100).all())

    def test_backlog_is_ranked_descending(self):
        scores = self.scored["opportunity_score"].tolist()
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_recommendation_has_required_fields(self):
        initiative = recommend_initiative(self.scored.iloc[0])
        self.assertEqual(set(initiative), {"initiative", "why", "metric"})


if __name__ == "__main__":
    unittest.main()
