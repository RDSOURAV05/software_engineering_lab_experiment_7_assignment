"""
Test-friendly entry point for the SafeAd AI Module (SAFE-VISION).

Classification uses the real SafeAdModelService.adapt_prediction() rules from
the main project. The heavy models (YOLO, BLIP, OCR, etc.) are not loaded
here, because they need a GPU and large downloads that CI cannot provide.
Instead, simulated evidence is derived from the file name and caption.
"""
from safead_adapter import SafeAdModelService

# Maps the project's internal class names to the labels used in the test plan
CATEGORY_LABELS = {
    "SAFE_FOR_ALL": "SAFE FOR ALL",
    "AGE_14_PLUS": "AGE 14+",
    "AGE_18_PLUS": "AGE 18+",
    "UNSAFE_FOR_ALL": "UNSAFE FOR ALL",
}

REVIEW_THRESHOLD = 50.0  # fused risk (0-100) at or above this goes to human review


def _simulate_evidence(name: str, caption: str):
    """Returns (fused_score, visual_risk, text_risk, violations) from filename/caption."""
    name = name.lower()
    text = (caption or "").lower()
    violations = []

    if "weapon" in name or "violence" in name:
        violations.append("Violence")
        visual, text_risk = 90.0, 70.0
    elif "alcohol" in name:
        violations.append("Alcohol/Tobacco")
        visual, text_risk = 45.0, 35.0
    else:
        visual, text_risk = 5.0, 5.0

    if "casino" in text or "gambling" in text:
        violations.append("Gambling")
        text_risk = max(text_risk, 40.0)

    fused = visual * 0.4 + text_risk * 0.6  # same 40/60 fusion as the real pipeline
    return fused, visual, text_risk, violations


def evaluate_ad(image_path, caption=None, score_override=None):
    """
    Classify an advertisement.
    score_override is a risk score from 0 to 1 (e.g. 0.5) used for boundary testing.
    """
    fused, visual, text_risk, violations = _simulate_evidence(image_path, caption)

    if score_override is not None:
        fused = float(score_override) * 100.0
        visual = fused
        text_risk = fused

    result = SafeAdModelService.adapt_prediction(
        fused_score=fused,
        visual_risk=visual,
        text_risk=text_risk,
        violations=violations,
        explanation_str=f"Automated evaluation of {image_path}",
    )

    result["category"] = CATEGORY_LABELS[result["classification"]]
    result["review"] = fused >= REVIEW_THRESHOLD
    return result