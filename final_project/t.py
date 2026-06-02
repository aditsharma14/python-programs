import requests

url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

payload = {
    "raw_document": {
        "text": "I am happy today"
    }
}

try:
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30
    )
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(e)