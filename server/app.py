from flask import Flask, jsonify, request
import sys
import uuid
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
movies_ref = db.collection('movies')


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("PONG MODAFUCKA!")


@app.route('/filmes', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        request.json['id'] = uuid.uuid4().hex
        movies_ref.document(request.json['id']).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/filmes', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        all_movies = [doc.to_dict() for doc in movies_ref.stream()]
        print(all_movies)
        return jsonify(all_movies), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/filmes', methods=['PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    print()
    try:
        id = request.json['movieID']
        movies_ref.document(id).update(request.json['data']['payload'])
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/filmes', methods=['DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        movie_id = request.args.get('id')
        movies_ref.document(movie_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == "__main__":
    app.run()
