from flask import Flask, jsonify, request
import sys
from flask_cors import CORS

MOVIES = [
    {"title": "Farewell", "author": "chinesa", "saw": True},
    {"title": "Fear and loathing", "author": "J. K. Rowling", "saw": False},
    {"title": "O poco", "author": "Dr. Seuss", "saw": True},
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


@app.route("/filmes", methods=["GET", "POST"])
def all_movies():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        MOVIES.append(
            {
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "saw": post_data.get("saw"),
            }
        )
        response_object["message"] = "Filme adicionado!"
    else:
        response_object["movies"] = MOVIES
    return jsonify(response_object)


if __name__ == "__main__":
    app.run()
