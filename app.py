from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/', methods=['POST'])
@app.route('/hdata.aspx', methods=['POST'])
def save_request():
    data = request.get_data(as_text=True)
    with open('requests.txt', 'a') as f:
        f.write(data + ',\n')
    return "Saved!", 200

@app.route('/getData', methods=['GET'])
def get_data():
    if not os.path.exists('requests.txt'):
        return "No data found", 404
    with open('requests.txt', 'r') as f:
        data = f.read()
        return data, 200
    return 'error occured', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)