import unittest

from marketing_systems_matrix import CampaignBrief, route_campaign


class CampaignRouterTests(unittest.TestCase):
    def test_routes_investor_material_to_review(self):
        route = route_campaign(CampaignBrief("possible investor", "update", 0.3))

        self.assertEqual(route.route, "investor_update")
        self.assertTrue(route.review_required)

    def test_rejects_bad_risk(self):
        route = route_campaign(CampaignBrief("builder", "demo", 2.0))

        self.assertEqual(route.route, "reject")

    def test_allows_low_risk_demo(self):
        route = route_campaign(CampaignBrief("builder", "demo", 0.2))

        self.assertEqual(route.route, "product_education")
        self.assertFalse(route.review_required)


if __name__ == "__main__":
    unittest.main()

