from flask import Flask , render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')