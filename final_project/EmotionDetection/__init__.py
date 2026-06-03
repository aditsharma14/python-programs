"""Emotion Detection package."""
from pathlib import Path
import sys

# Ensure the project root is available for imports when this file is executed directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from ..emotion_detection import emotion_detector
except ImportError:
    from emotion_detection import emotion_detector

__all__ = ["emotion_detector"]