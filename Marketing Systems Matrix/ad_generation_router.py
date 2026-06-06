class MediaAssetPipeline:
    """Hooks directly into Stable Diffusion / Midjourney APIs via Layer 1 clearance."""
    def generate_ad_prompt(self, target_demographic: str, room_style: str) -> str:
        base = "Photorealistic high-end digital illustration, neon ambient lighting, "
        if target_demographic == "vintage":
            return f"{base} classic arcade gaming layout, retro aesthetic style, 8k resolution"
        return f"{base} sleek minimalist modern online interface presentation, vibrant colors"
