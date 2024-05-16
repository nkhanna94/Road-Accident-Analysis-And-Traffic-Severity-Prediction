from flask import Flask, render_template, request
import random  # Import the random module for generating random numbers

app = Flask(__name__)

# Render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Handle the form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Generate a random number between 1 and 4
    random_number = random.randint(1, 4)

    # Render the result page with the random number
    return render_template('result.html', random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True)
