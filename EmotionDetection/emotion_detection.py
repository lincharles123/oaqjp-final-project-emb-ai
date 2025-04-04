import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=text)
    status_code = response.status_code
    data = json.loads(response.text)

    if status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        emotion_dict = data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        emotion_dict['dominant_emotion'] = dominant_emotion
    
    return emotion_dict