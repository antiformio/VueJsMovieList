from flask import Flask, jsonify, request
import sys
import uuid
from flask_cors import CORS

MOVIES = [
    {"id": uuid.uuid4().hex, "title": "Farewell", "author": "chinesa", "saw": True},
    {
        "id": uuid.uuid4().hex,
        "title": "Fear and loathing",
        "author": "J. K. Rowling",
        "saw": False,
    },
    {"id": uuid.uuid4().hex, "title": "O poco", "author": "Dr. Seuss", "saw": True},
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("PONG MODAFUCKA!")


# Add and fetch movies
@app.route("/filmes", methods=["GET", "POST"])
def all_movies():
    response_object = {"status": "success"}

    # Add movies
    if request.method == "POST":
        post_data = request.get_json()
        MOVIES.append(
            {
                "id": uuid.uuid4().hex,
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "saw": post_data.get("saw"),
            }
        )
        response_object["message"] = "Filme adicionado!"
    else:
        # Fetch movies
        response_object["movies"] = MOVIES
    return jsonify(response_object)


# Update and Delete Movies
@app.route("/filmes/<movie_id>", methods=["PUT", "DELETE"])
def single_movie(movie_id):
    response_object = {"status": "success"}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_movie(movie_id)
        MOVIES.append(
            {
                "id": uuid.uuid4().hex,
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "saw": post_data.get("saw"),
            }
        )
        response_object["message"] = "Filme Actualizado!"
    if request.method == "DELETE":
        remove_movie(movie_id)
        response_object["message"] = "Filme Apagado!"
    return jsonify(response_object)


# Aux function
def remove_movie(movie_id):
    for movie in MOVIES:
        if movie["id"] == movie_id:
            MOVIES.remove(movie)
            return True
    return False


if __name__ == "__main__":
    app.run()
