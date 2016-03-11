from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello CS-1122 TA's and Mr. Memon this is Shiv. I liked\
this assignment. It was interesting. :) "

if __name__ == "__main__":
    app.run(host = "10.0.2.15", port = 5000)
