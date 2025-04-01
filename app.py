from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_html():
    return send_file('index.html')

@app.route('/run_script')
def run_script():
    try:
        result = subprocess.run(
            ['python', 'mypy.py'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout or "Script executed successfully (no output)"
    except subprocess.CalledProcessError as e:
        return f"Script failed with error:\n{e.stderr}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
