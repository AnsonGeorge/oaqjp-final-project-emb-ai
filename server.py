from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def emotion_analyser(): # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')

# Pass the text to the sentiment_analyzer function and store the 
    response = emotion_detector(text_to_analyze)
# Extract the dominant value 
    dominant_value = response.split("'dominant_emotion':")[-1].strip(" '}")
# Return a formatted string with the sentiment label and score 
    return "For the given statement, the system response is {} The dominant emotion is {}.".format(response, dominant_value)

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

    