from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongo = PyMongo(app)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    mongo.db.todo_items.insert_one(data)
    return jsonify({"message": "To-Do item submitted successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
