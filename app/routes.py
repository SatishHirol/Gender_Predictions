from flask import Blueprint, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

main = Blueprint('main', __name__)

# Load the dataset
df = pd.read_csv('sex_height_weight.csv')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    # Use the trained model to make predictions
    model = LogisticRegression()
    model.fit(df[['Height', 'Weight']], df['Sex'])
    prediction = model.predict([[height, weight]])

    gender = 'Male' if prediction == 1 else 'Female'
    return render_template('result.html', gender=gender)