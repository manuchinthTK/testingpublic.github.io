from flask import Flask, jsonify, send_file
import subprocess
import sys

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_html():
    return send_file('index.html')

@app.route('/run_script')
def run_script():
    try:
        # Run the Python script with timeout (30 seconds)
        result = subprocess.run(
            [sys.executable, 'mypy.py'],  # Uses the same Python interpreter
            capture_output=True,
            text=True,
            timeout=30,  # Prevents hanging
            check=True
        )
        
        response = {
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        }
        return jsonify(response)
        
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Script timed out after 30 seconds'
        }), 500
        
    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': f'Script failed with return code {e.returncode}',
            'output': e.stdout,
            'stderr': e.stderr
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
