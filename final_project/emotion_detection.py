import requests

EMOTION_KEYS = ["anger", "disgust", "fear", "joy", "sadness"]
API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
API_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    if not isinstance(text_to_analyze, str):
        raise TypeError("text_to_analyze must be a string")

    payload = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(API_URL, json=payload, headers=API_HEADERS, timeout=10)
        
        # Handle blank entries (status_code 400)
        if response.status_code == 400:
            return {key: None for key in EMOTION_KEYS + ["dominant_emotion"]}
        
        response.raise_for_status()
        api_response = response.json()
    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            print("[DEBUG] API Endpoint returned 404")
            print(f"[DEBUG] URL: {API_URL}")
            print(f"[DEBUG] Headers: {API_HEADERS}")
            print(f"[DEBUG] Request body: {payload}")
            print(f"[DEBUG] Response: {e.response.text}")
        raise RuntimeError(f"Network error calling emotion API: {e}") from e
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Network error calling emotion API: {exc}") from exc

    def find_scores(data):
        if isinstance(data, dict):
            if all(key in data for key in EMOTION_KEYS):
                return {key: float(data[key]) for key in EMOTION_KEYS}
            for value in data.values():
                if isinstance(value, (dict, list)):
                    found = find_scores(value)
                    if found:
                        return found
        elif isinstance(data, list):
            for item in data:
                found = find_scores(item)
                if found:
                    return found
        return None

    scores = find_scores(api_response) or {key: 0.0 for key in EMOTION_KEYS}
    dominant_emotion = max(scores, key=scores.get) if scores else None
    return {**scores, "dominant_emotion": dominant_emotion}


if __name__ == "__main__":
    text = input("Enter text to analyze for emotion: ")
    try:
        result = emotion_detector(text)
        print("Emotion analysis result:", result)
    except RuntimeError as err:
        print(err)