from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/start-python', methods=['GET', 'POST'])  # Allow both GET & POST
def start_python():
    if request.method == 'POST':  # Ensure it's a POST request
        try:
            subprocess.run(["python", "mypy.py"], check=True)
            return "Python script executed successfully!"
        except subprocess.CalledProcessError:
            return "Error executing Python script!", 500
    return "Use POST method to start the script.", 405  # Return message if GET request is used

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
