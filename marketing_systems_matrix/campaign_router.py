from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CampaignBrief:
    audience: str
    offer_type: str
    risk_level: float
    channel: str = "organic"


@dataclass(frozen=True)
class CampaignRoute:
    route: str
    creative_direction: str
    review_required: bool
    reason: str


def route_campaign(brief: CampaignBrief) -> CampaignRoute:
    if not 0 <= brief.risk_level <= 1:
        return CampaignRoute("reject", "none", True, "risk_level must be between 0 and 1")

    if brief.risk_level >= 0.7:
        return CampaignRoute("compliance_review", "claim-substantiation", True, "risk level requires review")

    audience = brief.audience.strip().lower()
    offer = brief.offer_type.strip().lower()

    if "investor" in audience:
        return CampaignRoute("investor_update", "evidence-led operating narrative", True, "investor material needs review")

    if offer in {"demo", "prototype", "waitlist"}:
        return CampaignRoute("product_education", "clear value proof with measured claims", False, "low-risk product route")

    return CampaignRoute("brand_awareness", "AnarchI deterministic systems positioning", False, "general awareness route")

