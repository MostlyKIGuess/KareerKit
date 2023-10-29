from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your app

@app.route('/process_username', methods=['POST'])
def process_username():
    try:
        data = request.get_json()
        print("Received input data:")
        print(data) 
        return jsonify({"message": "Input data received"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
