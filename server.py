from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)

@app.route("/home")
def df_to_html():
    df = pd.read_csv("sample.csv")
    return df.to_html()

if __name__ == "__main__":
    app.run(debug=True)
