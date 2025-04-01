from flask import Flask, request
import subprocess

app = Flask(__name__)

# HTML content as a string
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Script Runner</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        button { padding: 10px 15px; font-size: 16px; }
        #output { margin-top: 20px; padding: 10px; border: 1px solid #ddd; min-height: 100px; }
    </style>
</head>
<body>
    <h1>Run Python Script</h1>
    <button onclick="runScript()">Run mypy.py</button>
    <div id="output">Output will appear here...</div>

    <script>
        function runScript() {
            document.getElementById('output').textContent = "Running script...";
            fetch('/run_script')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('output').textContent = data;
                })
                .catch(err => {
                    document.getElementById('output').textContent = "Error: " + err;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML

@app.route('/run_script')
def run_script():
    try:
        result = subprocess.run(['python', 'mypy.py'], 
                              capture_output=True, text=True)
        return result.stdout if result.stdout else "Script executed successfully (no output)"
    except Exception as e:
        return f"Error executing script: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
