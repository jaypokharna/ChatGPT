from flask import Flask, render_template , jsonify , request
from flask_pymongo import PyMongo

import openai

openai.api_key = "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"

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://cartoon276:jay276@chatgpt.5mqoaz4.mongodb.net/chatGPT"
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    chats = mongo.db.chats.find({})
    x = mongo.db
    myChats = [chat for chat in chats]
    return render_template("index.html",myChats = myChats)


@app.route("/api",methods = ["GET","POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")

        chat = mongo.db.chats.find_one({"question":question})
        if chat:
            data = {"answer":f"{chat['answer']}"}
            return jsonify(data)
        else :
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
            data = {"answer" : response["choices"][0]["text"]}
            mongo.db.chats.insert_one({"question":question , "answer" : response["choices"][0]["text"]})
            return jsonify(data)
    data = {"result":"Hello! How can I assist you today?"}
    return jsonify(data)


if __name__ == "__mian__":
    app.run(debug=False,host='0.0.0.0') 