"""
Unit tests for emotion detection application.
Tests the emotion_detector function with various text inputs
and validates the dominant_emotion output.
"""
import unittest
from unittest.mock import Mock, patch
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def _mock_response(self, json_data, status_code=200):
        """Helper method to create mock API responses."""
        mock_resp = Mock()
        mock_resp.status_code = status_code
        mock_resp.json.return_value = json_data
        mock_resp.raise_for_status.return_value = None
        return mock_resp

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_joy(self, mock_post):
        """Test: 'I am glad this happened' -> dominant_emotion: 'joy'"""
        mock_post.return_value = self._mock_response({
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.95,
            "sadness": 0.05,
        })

        result = emotion_detector("I am glad this happened")

        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_anger(self, mock_post):
        """Test: 'I am really mad about this' -> dominant_emotion: 'anger'"""
        mock_post.return_value = self._mock_response({
            "anger": 0.92,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.03,
            "sadness": 0.02,
        })

        result = emotion_detector("I am really mad about this")

        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_disgust(self, mock_post):
        """Test: 'I feel disgusted just hearing about this' -> dominant_emotion: 'disgust'"""
        mock_post.return_value = self._mock_response({
            "anger": 0.01,
            "disgust": 0.93,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.04,
        })

        result = emotion_detector("I feel disgusted just hearing about this")

        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_sadness(self, mock_post):
        """Test: 'I am so sad about this' -> dominant_emotion: 'sadness'"""
        mock_post.return_value = self._mock_response({
            "anger": 0.02,
            "disgust": 0.03,
            "fear": 0.05,
            "joy": 0.0,
            "sadness": 0.90,
        })

        result = emotion_detector("I am so sad about this")

        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_fear(self, mock_post):
        """Test: 'I am really afraid that this will happen' -> dominant_emotion: 'fear'"""
        mock_post.return_value = self._mock_response({
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.98,
            "joy": 0.01,
            "sadness": 0.01,
        })

        result = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
