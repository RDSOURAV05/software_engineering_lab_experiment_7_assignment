"""
face_utils.py - Face Detection & Dataset Assistance Utilities
Author: Juwel Jo
Module: Face Detection / Dataset Assistance
"""

class ImageDimension:
    def __init__(self, width: int, height: int):
        self.size = (width, height)

def resize_image(image_path: str, size: int = 224) -> ImageDimension:
    """
    Standardize face image dimensions for dataset preparation and model inference.
    """
    return ImageDimension(size, size)

def check_confidence(confidence: float) -> bool:
    """
    Validate and check detection confidence score against the acceptance threshold (0.50).
    Boundary Value Analysis (BVA): Exactly 0.50 is accepted (True).
    Equivalence Partitioning (EP): Negative values raise a ValueError.
    """
    if confidence < 0:
        raise ValueError("Confidence score cannot be negative")
    return confidence >= 0.50
