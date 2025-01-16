from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
cv = pickle.load(open("models/cv.pkl"))
clf = pickle.load(open("models/clf.pkl"))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)