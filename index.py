from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def random_acc():
    try:
        with open('api/acc.txt', 'r') as file:
            lines = file.readlines()
        if not lines:
            return jsonify({"status": "error", "message": "File is empty"}), 404
        random_line = random.choice(lines).strip()
        return jsonify({"status": "success", "data": random_line}), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "File not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
