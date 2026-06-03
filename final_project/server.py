"""Flask application for emotion detection API.

This module provides a web application that exposes endpoints for emotion
detection analysis using the Watson NLP API and a web-based user interface.
"""
from flask import Flask, jsonify, render_template, request

from emotion_detection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    """Render the home page with the emotion detection interface.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Process a POST request to analyze emotion from text.

    Expects a JSON payload with a 'text' field containing the text to analyze.
    Handles blank input by checking if dominant_emotion is None.

    Returns:
        Response: JSON response containing emotion scores and dominant emotion,
                  or error message with appropriate HTTP status code.
                  - 200: Success with emotion analysis result
                  - 400: Invalid request, input error, or blank text
                  - 502: API connection error
    """
    payload = request.get_json(silent=True)
    if not payload or "text" not in payload:
        return jsonify({"error": "Request body must be JSON with a 'text' field."}), 400

    text_to_analyze = payload["text"]
    try:
        result = emotion_detector(text_to_analyze)

        # Handle blank input: if dominant_emotion is None, return error
        if result.get("dominant_emotion") is None:
            return jsonify({"error": "Invalid text. Please provide a non-empty string."}), 400

        return jsonify(result)
    except TypeError as exc:
        return jsonify({"error": str(exc)}), 400
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
