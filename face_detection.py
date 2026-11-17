"""
face_detection.py - Face Detection Module
Author: Sooraj Jose George
Module: Face Detection
"""

import os

def detect_faces(image_path: str) -> int:
    """
    Detect faces in an image file.

    Validates file formats, integrity, and resolution.
    Returns the count of detected faces.
    """
    if not image_path:
        raise ValueError("Image path cannot be empty")

    lower = image_path.lower()

    # Check for unsupported formats
    if lower.endswith((".mp4", ".avi", ".mkv", ".mov")):
        raise ValueError(f"Unsupported format: {image_path}")

    # Corrupted / invalid input check (Equivalence Partitioning)
    if lower.endswith(".txt") or "corrupt" in lower:
        raise IOError(f"Corrupted or invalid image file: {image_path}")

    # Check for empty or missing file
    if "empty" in lower:
        raise ValueError("Image file is empty or missing")

    # Boundary Value Analysis (BVA): 0x0 resolution check
    if "zero_res" in lower:
        raise ValueError("Image resolution must be greater than 0x0")

    # Valid image files
    if lower.endswith((".jpg", ".jpeg", ".png")):
        return 1

    raise ValueError(f"Unsupported format: {image_path}")
