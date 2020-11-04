from flask import Flask, request, json, jsonify, Response, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/predict', methods=['POST'])
def post_route():
    print(request.form)
    data = request.form
    # Make all form fields ternarys checking for type
    fuel_consumption = data["fuel_consumption"] if isinstance(data["fuel_consumption"], float) else None
    cylinders = data["cylinders"]
    engine_size = data["engine_size"]
    # If invalid data, send back form with error message
    # Instantiate model (linear regression) from model file
    # Return prediction
    return render_template('fuel_prediction.html', prediction=3)

@app.route('/get')
def index_route():
    return "Test 2"