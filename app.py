from flask import Flask
import os

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!"
@app.route("/bye")
def bye():
    return "Good bye world!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True,host='0.0.0.0',port=port)
