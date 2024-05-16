from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open(r'D:\Python\severity_prediction\WebApp\xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Render the index page
@app.route('/')
def index():
	@@ -16,41 +11,11 @@ def index():
# Handle the form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    distance = request.form['distance']
    street = request.form['street']
    city = request.form['city']
    country = request.form['country']
    state = request.form['state']
    temperature = request.form['temperature']
    wind_chill = request.form['wind_chill']
    visibility = request.form['visibility']
    wind_direction = request.form['wind_direction']
    weather_condition = request.form['weather_condition']
    traffic_signal = request.form['traffic_signal']
    sunrise_sunset = request.form['sunrise_sunset']

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'distance': [distance],
        'street': [street],
        'city': [city],
        'country': [country],
        'state': [state],
        'temperature': [temperature],
        'wind_chill': [wind_chill],
        'visibility': [visibility],
        'wind_direction': [wind_direction],
        'weather_condition': [weather_condition],
        'traffic_signal': [traffic_signal],
        'sunrise_sunset': [sunrise_sunset]
    })

    # Use the trained model to make a prediction
    prediction = model.predict(input_data)[0]

    # Render the result page with the prediction
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
