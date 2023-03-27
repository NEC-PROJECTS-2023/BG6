from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='template')

model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return render_template('health.html')


@app.route('/predict', methods = ["POST", "GET"])
def predict():
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoke = int(request.form['smoke'])
    region = int(request.form['region'])
    result = model.predict([[age, gender, bmi, children, smoke, region]])
    return render_template('submit.html',  result="$ {:.2f}".format(result[0]))


if __name__ == '__main__':
    app.run(debug=True)
