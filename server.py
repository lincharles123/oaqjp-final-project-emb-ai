"""Flask app for Emotion Detection"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    """Render the index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent():
    """Analyze text and return detected emotions"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is not None:
        result_str = "For the given statement, the system response is "
        emotions = [emotion for emotion in response if emotion != "dominant_emotion"]

        for emotion in emotions[:-2]:
            result_str += f"'{emotion}': {response[emotion]}, "

        result_str += f"'{emotions[-2]}': {response[emotions[-2]]} and "
        result_str += f"'{emotions[-1]}': {response[emotions[-1]]}. "
        result_str += f"The dominant emotion is {response['dominant_emotion']}."
    else:
        result_str = "Invalid text! Please try again!"

    return result_str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
