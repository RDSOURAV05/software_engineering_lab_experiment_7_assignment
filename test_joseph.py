import pytest
from ai_moderation import evaluate_ad

# Test 1: Standard safe ad
def test_safe_ad():
    assert evaluate_ad("safe_ad.jpg")['category'] == "SAFE FOR ALL"

# Test 2: Unsafe ad classification
def test_unsafe_ad():
    assert evaluate_ad("weapon.jpg")['category'] == "UNSAFE FOR ALL"

# Test 3: Age restricted ad
def test_age_18_ad():
    assert evaluate_ad("alcohol.jpg")['category'] == "AGE 18+"

# Test 4: Risk score exactly at threshold of 0.5 (Boundary Value Analysis)
def test_risk_threshold_boundary():
    assert evaluate_ad("borderline.jpg", score_override=0.5)['review'] == True

# Test 5: Missing caption/text (Equivalence Partitioning)
def test_missing_caption():
    assert evaluate_ad("image_only.jpg", caption="") is not None