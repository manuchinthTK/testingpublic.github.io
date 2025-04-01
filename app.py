from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-python', methods=['POST'])
def start_python():
    try:
        subprocess.run(["python", "mypy.py"], check=True)
        return "Python script executed successfully!"
    except subprocess.CalledProcessError:
        return "Error executing Python script!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
