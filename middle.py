from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True # change to false when deploying
    app.secret_key = str(uuid4())
    app.run()
