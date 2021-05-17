from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'HI'

if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    #util.load_saved_artifacts()
    app.run()
    