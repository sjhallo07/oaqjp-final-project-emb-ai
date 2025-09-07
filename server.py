from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == 'GET':
        text = request.args.get('textToAnalyze')
    else:
        text = request.form.get('textToAnalyze')

    if not text or text.strip() == '':
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    try:
        result = emotion_detector(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
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