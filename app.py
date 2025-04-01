from flask import Flask, jsonify, send_file
import subprocess
import sys
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_html():
    return send_file('index.html')

@app.route('/run_script')
def run_script():
    try:
        result = subprocess.run(
            [sys.executable, 'mypy.py'],
            capture_output=True,
            text=True,
            timeout=30,
            check=True
        )
        
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
        
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Script timed out after 30 seconds'
        }), 500
        
    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': f'Script failed (code {e.returncode})',
            'output': e.stdout,
            'stderr': e.stderr
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
