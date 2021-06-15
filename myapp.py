from flask import Flask 
app = Flask(__name__)

@app.route("/index")
def home():
    return "Hallo ini Flask"

if __name__ == "__main__":
    app.run(debug=True)