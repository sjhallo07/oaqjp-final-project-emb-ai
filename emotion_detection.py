import requests

def emotion_detector(text_to_analyze):
    # solicitud POST
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    
    try:
        #  POST
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        
        # código de estado
        if response.status_code == 200:
            return response.text  # respuesta
        else:
            return f"Error: Received status code {response.status_code}. Response: {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

# Para probar la función 
if __name__ == "__main__":
    # Prueba co
    result = emotion_detector("Me encanta esta nueva tecnología")
    print(result)