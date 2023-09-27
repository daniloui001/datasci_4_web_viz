import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

newyork = pd.read_csv("https://raw.githubusercontent.com/daniloui001/datasci_4_web_viz/main/Healthy%20People%20New%20York.csv")
alabama = pd.read_csv("https://raw.githubusercontent.com/daniloui001/datasci_4_web_viz/main/Healthy%20People%20Alabama.csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


