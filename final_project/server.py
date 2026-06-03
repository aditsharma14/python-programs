"""Flask application for emotion detection API.

This module provides a web application that exposes endpoints for emotion
detection analysis using the Watson NLP API and a web-based user interface.
"""
from flask import Flask, render_template, request, jsonify

from emotion_detection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")


def validate_and_analyze(text_to_analyze):
    """Validate text and perform emotion detection analysis.

    Args:
        text_to_analyze: The text to analyze for emotions.

    Returns:
        tuple: (response_dict, status_code)

    Raises:
        TypeError: If text is not a string.
        RuntimeError: If API call fails.
    """
    try:
        result = emotion_detector(text_to_analyze)
        if result.get("dominant_emotion") is None:
            return {"error": "Invalid text! Please try again!"}, 400

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
        return {"result": response_text}, 200
    except TypeError:
        return {"error": "Invalid text! Please try again!"}, 400
    except RuntimeError as exc:
        return {"error": f"Network error calling emotion API: {str(exc)}"}, 502


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

    Returns:
        Response: JSON response containing emotion analysis or error message
                  with appropriate HTTP status code.
    """
    payload = request.get_json(silent=True)
    if not payload or "text" not in payload:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    text_to_analyze = payload["text"]

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response, status_code = validate_and_analyze(text_to_analyze)
    return jsonify(response), status_code


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
