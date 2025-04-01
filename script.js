// Add to script.js
function checkResults() {
    fetch('https://raw.githubusercontent.com/manuchinthTK/testingpublic.github.io/main/scripts/output.txt?t=${Date.now()}')
        .then(r => r.text())
        .then(t => {
            if(t.trim()) {
                document.getElementById('output').textContent = t;
                clearInterval(pollInterval);
            }
        });
}

let pollInterval;
function runWithAutoRefresh() {
    showInstructions();
    pollInterval = setInterval(checkResults, 5000); // Check every 5 sec
}
