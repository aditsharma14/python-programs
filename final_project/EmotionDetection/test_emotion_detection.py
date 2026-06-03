import os
import sys
import unittest
from unittest.mock import Mock, patch

# Ensure project root (parent of this package) is on sys.path so tests can import
# the top-level `emotion_detection.py` module regardless of current working dir.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def _mock_response(self, json_data, status_code=200):
        mock_resp = Mock()
        mock_resp.status_code = status_code
        mock_resp.json.return_value = json_data
        mock_resp.raise_for_status.return_value = None
        return mock_resp

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_joy(self, mock_post):
        mock_post.return_value = self._mock_response({
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.95,
            "sadness": 0.05,
        })

        result = emotion_detector("I am glad this happened")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.95)

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_anger(self, mock_post):
        mock_post.return_value = self._mock_response({
            "anger": 0.92,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.03,
            "sadness": 0.02,
        })

        result = emotion_detector("I am really mad about this")

        self.assertEqual(result["dominant_emotion"], "anger")
        self.assertEqual(result["anger"], 0.92)

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_disgust(self, mock_post):
        mock_post.return_value = self._mock_response({
            "anger": 0.01,
            "disgust": 0.93,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.04,
        })

        result = emotion_detector("I feel disgusted just hearing about this")

        self.assertEqual(result["dominant_emotion"], "disgust")
        self.assertEqual(result["disgust"], 0.93)

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_sadness(self, mock_post):
        mock_post.return_value = self._mock_response({
            "anger": 0.02,
            "disgust": 0.03,
            "fear": 0.05,
            "joy": 0.0,
            "sadness": 0.90,
        })

        result = emotion_detector("I am so sad about this")

        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertEqual(result["sadness"], 0.90)

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_fear(self, mock_post):
        mock_post.return_value = self._mock_response({
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.98,
            "joy": 0.01,
            "sadness": 0.01,
        })

        result = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(result["dominant_emotion"], "fear")
        self.assertEqual(result["fear"], 0.98)


if __name__ == "__main__":
    unittest.main()
