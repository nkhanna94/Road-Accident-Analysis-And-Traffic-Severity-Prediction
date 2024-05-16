from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
import traceback
import pickle

app = Flask(__name__)
@app.route('/')
def index():
    return render_template(r'D:\Python\severity_prediction\WebApp\templates\index.html')


if __name__ == '__main__':
    app.run(debug=True)
