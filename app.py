from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load models with error handling
try:
    with open("models/cv.pkl", "rb") as cv_file:
        cv = pickle.load(cv_file)
    with open("models/clf.pkl", "rb") as clf_file:
        clf = pickle.load(clf_file)
except FileNotFoundError as e:
    print(f"Error: {e}. Ensure the 'models/' directory contains 'cv.pkl' and 'clf.pkl'.")
    exit()
except pickle.UnpicklingError as e:
    print(f"Error loading pickle file: {e}. Check if the files are in the correct format.")
    exit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        email = request.form.get('content')
        tokenized_email = cv.transform([email])  # Transform input text
        prediction = clf.predict(tokenized_email)
        prediction = 1 if prediction == 1 else -1
        return render_template("index.html", prediction=prediction, email=email)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
