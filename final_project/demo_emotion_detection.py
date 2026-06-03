"""
Demonstration script showing import and emotion detection output.
"""
from EmotionDetection.emotion_detection import emotion_detector

# Test the emotion detector with various emotions
test_cases = [
    "I am glad this happened",
    "I am really mad about this",
    "I feel disgusted just hearing about this",
    "I am so sad about this",
    "I am really afraid that this will happen"
]

print("=" * 70)
print("EMOTION DETECTION DEMONSTRATION")
print("=" * 70)
print()

for text in test_cases:
    print(f"Input: {text}")
    result = emotion_detector(text)
    print(f"Output: {result}")
    print("-" * 70)
