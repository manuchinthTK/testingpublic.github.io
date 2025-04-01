document.getElementById('runBtn').addEventListener('click', async () => {
    const output = document.getElementById('output');
    output.textContent = "Starting execution...";

    try {
        const response = await fetch('https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/dispatches', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github.everest-preview+json',
                'Authorization': 'token YOUR_GITHUB_TOKEN',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ event_type: 'run_python_script' })
        });

        if (response.ok) {
            output.textContent = "Workflow triggered! Waiting for results...";
            setTimeout(checkResults, 5000); // Wait before checking results
        } else {
            output.textContent = "Error: " + (await response.text());
        }
    } catch (error) {
        output.textContent = `Error: ${error.message}`;
    }
});

async function checkResults() {
    const output = document.getElementById('output');
    const response = await fetch(
        'https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/scripts/output.txt?t=' + Date.now()
    );
    output.textContent = await response.text();
}
