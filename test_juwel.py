# Create this file in your project folder and name it: test_juwel.py
import pytest
from face_utils import resize_image, check_confidence

# Test 1: Standard resize behavior
def test_resize_standard():
    assert resize_image("face.jpg", 224).size == (224, 224)

# Test 2: High confidence passing
def test_confidence_high():
    assert check_confidence(0.95) == True

# Test 3: Low confidence failing
def test_confidence_low():
    assert check_confidence(0.30) == False

# Test 4: Confidence exactly at threshold 0.5 (Boundary Value Analysis)
def test_confidence_boundary():
    assert check_confidence(0.50) == True 

# Test 5: Negative confidence value (Equivalence Partitioning)
def test_invalid_confidence():
    with pytest.raises(ValueError):
        check_confidence(-0.1)
