import requests
import json

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
   
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
       
        response = requests.post(url, headers=headers, json=payload)
        
        
        if response.status_code == 200:
         
            response_dict = json.loads(response.text)
            
            
            emotions = response_dict['emotionPredictions'][0]['emotion']
            
           
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
           
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
           
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
           
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            
            return {"error": f"Received status code {response.status_code}"}
    
    except requests.exceptions.RequestException as e:
        
        return {"error": f"An error occurred: {str(e)}"}