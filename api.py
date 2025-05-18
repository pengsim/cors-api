from flask import Flask , jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/index')
def index():
    return jsonify({
        'message' : 'connect successfully ! welcome to my api'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
