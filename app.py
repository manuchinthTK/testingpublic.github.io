from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    try:
        # Execute the Python script
        result = subprocess.run(['python', 'mypy.py'], capture_output=True, text=True)
        return result.stdout if result.stdout else "Script executed successfully!"
    except Exception as e:
        return f"Error executing script: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
