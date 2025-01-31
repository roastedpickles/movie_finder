from flask import Flask, render_template, jsonify
import requests
import random
import os

app = Flask(__name__)

OMDB_API_KEY = "d106887b"  # Remplacez par votre clé API OMDB
OMDB_API_URL = "http://www.omdbapi.com/?i=tt3896198&apikey=d106887b"
PICSUM_URL = "https://picsum.photos/200/300"

MOVIES = ["Inception", "The Matrix", "Interstellar", "Fight Club", "The Dark Knight"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random_movie")
def get_random_movie():
    movie_title = random.choice(MOVIES)
    params = {"t": movie_title, "apikey": OMDB_API_KEY}
    response = requests.get(OMDB_API_URL)
    movie_data = response.json()

    if movie_data["Response"] == "True":
        return jsonify({
            "title": movie_data["Title"],
            "description": movie_data["Plot"],
            "image": PICSUM_URL
        })
    else:
        return jsonify({"error": "Movie not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
