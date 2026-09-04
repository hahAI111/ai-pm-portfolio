import pathlib
import sys
import unittest

import pandas as pd

sys.path.append(str(pathlib.Path(__file__).parent))
from support_engine import classify_ticket, draft_response, retrieve_guidance


class SellerSupportTests(unittest.TestCase):
    def setUp(self):
        root = pathlib.Path(__file__).parent
        self.knowledge_base = pd.read_csv(root / "seller_knowledge_base.csv")

    def test_policy_ticket_requires_human_review(self):
        result = classify_ticket("Can I make this health claim in my product description?")
        self.assertEqual(result["category"], "Policy")
        self.assertTrue(result["escalation"])

    def test_advertising_ticket_is_classified(self):
        result = classify_ticket("Which advertising keywords should I pause when ROAS is declining?")
        self.assertEqual(result["category"], "Advertising")

    def test_policy_response_is_safe(self):
        classification = classify_ticket("Can I make this health claim?")
        guidance = retrieve_guidance(self.knowledge_base, classification["category"])
        response = draft_response("Can I make this health claim?", classification, guidance)
        self.assertIn("human review", response.lower())


if __name__ == "__main__":
    unittest.main()
