"""Flask application for emotion detection API.

This module provides a web application that exposes endpoints for emotion
detection analysis using the Watson NLP API and a web-based user interface.
"""
from flask import Flask, render_template, request

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
    Validates that input is not blank, empty, or whitespace-only.
    Handles blank input by returning appropriate error message.
    Formats the response as a readable string with emotion scores and dominant emotion.

    Returns:
        Response: Formatted string response containing emotion analysis
                  or error message with appropriate HTTP status code.
                  - 200: Success with formatted emotion analysis result
                  - 400: Invalid request, input error, or blank text
                  - 502: API connection error
    """
    payload = request.get_json(silent=True)
    if not payload or "text" not in payload:
        return "Request body must be JSON with a 'text' field.", 400

    text_to_analyze = payload["text"]

    # Validate blank input: check for None, empty string, or whitespace-only
    if text_to_analyze is None or not isinstance(text_to_analyze, str):
        return "Invalid text. Please provide a non-empty string.", 400

    if text_to_analyze.strip() == "":
        return "Invalid text. Please provide a non-empty string.", 400

    try:
        result = emotion_detector(text_to_analyze)

        # Handle blank input error from emotion_detector: if dominant_emotion is None
        if result.get("dominant_emotion") is None:
            return "Invalid text. Please provide a non-empty string.", 400

        # Format the response as per customer requirements
        anger = result.get("anger")
        disgust = result.get("disgust")
        fear = result.get("fear")
        joy = result.get("joy")
        sadness = result.get("sadness")
        dominant_emotion = result.get("dominant_emotion")

        response_text = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is **{dominant_emotion}**."
        )

        return response_text, 200
    except TypeError as exc:
        return f"Invalid text. Please provide a non-empty string.", 400
    except RuntimeError as exc:
        return f"Network error calling emotion API: {str(exc)}", 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
