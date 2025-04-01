from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/trigger-workflow', methods=['POST'])
def trigger_workflow():
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        return jsonify({"error": "Missing GitHub token"}), 500

    headers = {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {"event_type": "run_python_script"}

    response = requests.post(
        'https://api.github.com/repos/manuchinthTK/testingpublic.github.io/dispatches',
        headers=headers,
        json=payload
    )

    if response.status_code == 204:
        return jsonify({"message": "Workflow triggered successfully"})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
