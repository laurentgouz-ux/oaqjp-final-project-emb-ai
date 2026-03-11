"""
Serveur Flask pour l'application de détection d'émotions.
Ce module définit les routes pour l'interface utilisateur et l'appel à l'API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyse le texte fourni par l'utilisateur et renvoie les scores d'émotions.
    """
    # Récupérer le texte de la requête
    text_to_analyze = request.args.get('textToAnalyze')

    # Appeler la fonction du package
    response = emotion_detector(text_to_analyze)

    # Extraction de l'émotion dominante
    dominant_emotion = response['dominant_emotion']

    # Logique de gestion d'erreur (Tâche 7)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Formatage de la réponse
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Affiche la page d'accueil de l'application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
