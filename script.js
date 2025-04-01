async function runScript() {
    const outputDiv = document.getElementById('output');
    outputDiv.textContent = "Triggering GitHub Actions workflow...";
    
    try {
        // This URL will trigger the workflow dispatch event
        const response = await fetch(
            `https://api.github.com/repos/manuchinthTK/testingpublic.github.io/workflows/run_script.yml/dispatches`,
            {
                method: 'POST',
                headers: {
                    'Authorization': 'token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',
                    'Accept': 'application/vnd.github.v3+json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ref: 'main'  // or your branch name
                })
            }
        );
        
        if (response.ok) {
            outputDiv.textContent = "Workflow triggered successfully! Checking results in 30 seconds...";
            setTimeout(checkResults, 30000);
        } else {
            outputDiv.textContent = `Error triggering workflow: ${response.status}`;
        }
    } catch (error) {
        outputDiv.textContent = `Error: ${error.message}`;
    }
}

async function checkResults() {
    const outputDiv = document.getElementById('output');
    try {
        // Fetch the output file directly from GitHub
        const response = await fetch(
            'https://raw.githubusercontent.com/manuchinthTK/testingpublic.github.io/main/scripts/output.txt'
        );
        const text = await response.text();
        outputDiv.textContent = text || "No output generated";
    } catch (error) {
        outputDiv.textContent = `Error fetching results: ${error.message}`;
    }
}
