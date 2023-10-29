from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/signin_db"
mongo = PyMongo(app)

@app.route('/api/signin', methods=['POST'])
def signin():
    user_data = request.get_json()
    users = mongo.db.users
    users.insert_one(user_data)
    return jsonify({"message": "User signed in successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
