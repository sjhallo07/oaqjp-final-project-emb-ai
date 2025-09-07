"""
Módulo principal del servidor Flask para detección de emociones.
Este módulo proporciona endpoints RESTful para analizar emociones en texto.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Endpoint principal que sirve la página web inicial.

    Returns:
        str: HTML de la página inicial renderizada desde la plantilla index.html
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Endpoint para analizar emociones en texto proporcionado.

    Supports:
        GET: Recibe texto a través del parámetro de consulta 'text'
        POST: Recibe texto en el cuerpo de la solicitud en formato JSON

    Returns:
        JSON: Resultado del análisis de emociones o mensaje de error
    """
    # Obtener el texto de la solicitud según el método
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text') if data else None
    else:  # GET
        text_to_analyze = request.args.get('text')

    # Verificar si no se proporcionó texto
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            "error": "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"
        }), 400

    # Realizar el análisis de emociones
    result = emotion_detector(text_to_analyze)

    # Verificar si hubo un error en el análisis
    if 'error' in result:
        return jsonify({"error": result['error']}), 500

    # Verificar si la emoción dominante es None (entrada inválida)
    if result['dominant_emotion'] is None:
        return jsonify({
            "error": "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"
        }), 400

    # Crear la cadena de texto descriptiva según el formato solicitado
    descriptive_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Retornar la respuesta en formato JSON
    return jsonify({
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion'],
        "output": descriptive_text
    })

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

    