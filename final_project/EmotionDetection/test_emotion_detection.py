import os
import sys

# Ensure project root (parent of this package) is on sys.path so tests can import
# the top-level `emotion_detection.py` module regardless of current working dir.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from emotion_detection import emotion_detector

emotion_detector("I am glad this happened")
emotion_detector("I am really mad about this")	
emotion_detector("I feel disgusted just hearing about this")	
emotion_detector("I am so sad about this")
emotion_detector("I am really afraid that this will happen")