import requests
import json

def emotion_detector(text_to_analyze):
    # URL para la solicitud POST
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Cuerpo de la solicitud en formato JSON
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
        # Realizar la solicitud POST
        response = requests.post(url, headers=headers, json=payload)
        
        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Convertir la respuesta JSON a diccionario
            response_dict = json.loads(response.text)
            
            # Extraer las emociones de la estructura real de la respuesta
            emotions = response_dict['emotionPredictions'][0]['emotion']
            
            # Extraer los puntajes de cada emoción
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Encontrar la emoción dominante
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # Encontrar la emoción con el puntaje más alto
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Retornar el formato requerido
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # Retornar mensaje de error con el código de estado
            return {"error": f"Received status code {response.status_code}"}
    
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión o de solicitud
        return {"error": f"An error occurred: {str(e)}"}

# Este bloque debe estar FUERA de la función
if __name__ == "__main__":
    # Prueba de la función
    result = emotion_detector("Me encanta esta nueva tecnología")
    print(result)