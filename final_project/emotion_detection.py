import requests

EMOTION_KEYS = ["anger", "disgust", "fear", "joy", "sadness"]

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict/'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Network error calling emotion API: {exc}") from exc


def extract_emotion_scores(api_response):
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
    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }


if __name__ == "__main__":
    text = input("Enter text to analyze for emotion: ")
    try:
        api_response = emotion_detector(text)
        formatted_result = extract_emotion_scores(api_response)
        print("Emotion analysis result:", formatted_result)
    except RuntimeError as err:
        print(err)