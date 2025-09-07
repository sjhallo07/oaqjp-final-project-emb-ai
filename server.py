from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
   
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text') if data else None
    else:  
        text_to_analyze = request.args.get('text')
    
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            "error": "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"
        }), 400
    
   
    result = emotion_detector(text_to_analyze)
    
    
    if 'error' in result:
        return jsonify({"error": result['error']}), 500

    
    if result['dominant_emotion'] is None:
        return jsonify({
            "error": "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"
        }), 400
    
    
    descriptive_text = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    
    
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