async function runScript() {
    const outputDiv = document.getElementById('output');
    outputDiv.textContent = "Triggering GitHub Actions...";

    try {
        // Replace with YOUR Personal Access Token (PAT)
        const PAT = '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'; // ⚠️ Never commit real tokens!
        
        const response = await fetch(
            'https://api.github.com/repos/manuchinthTK/testingpublic.github.io/actions/workflows/run_script.yml/dispatches',
            {
                method: 'POST',
                headers: {
                    'Authorization': `token ${PAT}`,
                    'Accept': 'application/vnd.github.v3+json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ref: 'main' }), // Branch name
            }
        );

        if (response.ok) {
            outputDiv.textContent = "Workflow triggered! Refreshing in 30s...";
            setTimeout(checkResults, 30000); // Check back later
        } else {
            const error = await response.json();
            outputDiv.textContent = `Error: ${error.message}`;
        }
    } catch (error) {
        outputDiv.textContent = `Failed: ${error.message}`;
    }
}

async function checkResults() {
    const outputDiv = document.getElementById('output');
    try {
        // Fetch the latest output from GitHub
        const response = await fetch(
            'https://raw.githubusercontent.com/manuchinthTK/testingpublic.github.io/main/scripts/output.txt'
        );
        const result = await response.text();
        outputDiv.textContent = result || "No output yet.";
    } catch (error) {
        outputDiv.textContent = `Error fetching results: ${error.message}`;
    }
}
