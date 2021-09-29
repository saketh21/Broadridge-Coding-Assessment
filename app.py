from flask import Flask
from flask import jsonify
from datetime import datetime


# datetime object containing current date and time
now = datetime.now()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def message():
    return jsonify({'Message': 'My name is Saketh Gurumurthi', 'Received Timestamp': now.strftime("%d/%m/%Y %H:%M:%S")})
if __name__ == "__main__":
    app.run(debug=True)

