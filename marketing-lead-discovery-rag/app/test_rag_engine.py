import pathlib
import sys
import unittest

import pandas as pd

sys.path.append(str(pathlib.Path(__file__).parent))
from rag_engine import build_profile, evaluate_golden_dataset, rerank_candidates, retrieve_candidates


class LeadDiscoveryRagTests(unittest.TestCase):
    def setUp(self):
        root = pathlib.Path(__file__).parent
        self.sources = pd.read_csv(root / "sample_lead_sources.csv")
        self.golden = pd.read_csv(root / "golden_dataset.csv")

    def test_retrieves_expected_lead(self):
        query = "Which company is expanding marketplace fulfillment?"
        ranked = rerank_candidates(retrieve_candidates(self.sources, query), query)
        self.assertIn("L1001", ranked["lead_id"].tolist())

    def test_reranking_limits_context(self):
        ranked = rerank_candidates(retrieve_candidates(self.sources, "marketplace"), "marketplace")
        self.assertLessEqual(len(ranked), 3)

    def test_golden_set_has_retrieval_signal(self):
        result = evaluate_golden_dataset(self.sources, self.golden)
        self.assertGreater(result["lead_retrieved"].mean(), 0.5)

    def test_profile_citations_belong_to_selected_lead(self):
        query = "Which company is expanding marketplace fulfillment?"
        profile = build_profile(rerank_candidates(retrieve_candidates(self.sources, query), query))
        self.assertEqual(profile["company_name"], "Northstar Home")
        self.assertTrue(all(citation["source_id"] in {"S001", "S002"} for citation in profile["citations"]))


if __name__ == "__main__":
    unittest.main()
