import unittest

from marketing_systems_matrix import CampaignBrief, build_launch_plan


class LaunchPlanTests(unittest.TestCase):
    def test_investor_plan_requires_proof_assets_and_blocks_sensitive_claims(self):
        plan = build_launch_plan(CampaignBrief("investor", "update", 0.3))

        self.assertEqual(plan.route.route, "investor_update")
        self.assertIn("IP ledger hashes", plan.proof_assets)
        self.assertIn("unfiled patent specifics", plan.blocked_claims)

    def test_high_risk_plan_routes_to_compliance_sequence(self):
        plan = build_launch_plan(CampaignBrief("public", "claim", 0.9))

        self.assertEqual(plan.route.route, "compliance_review")
        self.assertEqual(plan.sequence[0], "collect proof")

    def test_demo_plan_is_customer_education(self):
        plan = build_launch_plan(CampaignBrief("builder", "demo", 0.2))

        self.assertEqual(plan.route.route, "product_education")
        self.assertIn("demo proof", plan.sequence)

    def test_invalid_risk_blocks_launch(self):
        plan = build_launch_plan(CampaignBrief("builder", "demo", -1))

        self.assertEqual(plan.headline, "Blocked pending corrected risk input")
        self.assertEqual(plan.sequence, ())


if __name__ == "__main__":
    unittest.main()
