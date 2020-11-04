from flask import Flask, request, json, jsonify, Response, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/post', methods=['POST'])
def post_route():
    print(request)
    return "Got it"

@app.route('/get')
def index_route():
    return "Test 2"