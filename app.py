from flask import Flask , render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST' , 'GET'])
def predict_datapoints():
    if request.method == "GET":
        return render_template('home.html')
    else:
        pass


if __name__ == '__main__':
    app.run()
