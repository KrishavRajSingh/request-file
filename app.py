from flask import Flask, request

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_request():
    data = request.get_data(as_text=True)
    with open('requests.txt', 'a') as f:
        f.write(data + ',\n')
    return "Saved!", 200

@app.route('/getData', methods=['GET'])
def get_data():
    with open('requests.txt', 'r') as f:
        data = f.read()
    return data, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
