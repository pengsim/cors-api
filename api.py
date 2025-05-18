from flask import Flask , jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/index')
def index():
    return jsonify({
        'message' : 'connect successfully !'
    })

if __name__ == '__main__':
    app.run(debug=True)