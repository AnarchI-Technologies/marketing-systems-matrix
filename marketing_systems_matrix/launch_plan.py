from __future__ import annotations

from dataclasses import dataclass

from .campaign_router import CampaignBrief, CampaignRoute, route_campaign


@dataclass(frozen=True)
class LaunchPlan:
    route: CampaignRoute
    headline: str
    sequence: tuple[str, ...]
    proof_assets: tuple[str, ...]
    blocked_claims: tuple[str, ...]


def build_launch_plan(brief: CampaignBrief) -> LaunchPlan:
    route = route_campaign(brief)

    if route.route == "reject":
        return LaunchPlan(route, "Blocked pending corrected risk input", (), (), ("unbounded risk claims",))

    if route.route == "compliance_review":
        return LaunchPlan(
            route,
            "Evidence review before public claims",
            ("collect proof", "substantiate claims", "human approval", "publish conservative update"),
            ("test results", "commit hashes", "before/after summary"),
            ("guaranteed outcomes", "unsupported legal/financial claims"),
        )

    if route.route == "investor_update":
        return LaunchPlan(
            route,
            "AnarchI operating systems are becoming productized proof assets",
            ("repo evidence", "product surfaces", "traction narrative", "next capital use"),
            ("published repos", "test results", "IP ledger hashes"),
            ("unfiled patent specifics", "unverified revenue claims"),
        )

    if route.route == "product_education":
        return LaunchPlan(
            route,
            "See the deterministic system before the pitch",
            ("problem frame", "demo proof", "safe offer", "invite to trial"),
            ("demo script", "package dry-run", "test suite"),
            ("autonomous guarantees", "customer data claims"),
        )

    return LaunchPlan(
        route,
        "Hardcoding freedom into the systems of tomorrow",
        ("brand thesis", "public-safe proof", "product path", "community ask"),
        ("architecture map", "README", "public dashboard"),
        ("secret logic", "unsupported market dominance claims"),
    )
