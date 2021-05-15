from flask import Flask, request, jsonify
#import util

app = Flask(__name__)

if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    #util.load_saved_artifacts()
    app.run()
    