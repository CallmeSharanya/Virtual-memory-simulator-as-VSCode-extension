const vscode = require('vscode');
const { spawn } = require('child_process');

function activate(context) {
	let disposable = vscode.commands.registerCommand('extension.showMemoryInsights', function () {
		const panel = vscode.window.createWebviewPanel(
			'memoryInsights',
			'Memory Insights',
			vscode.ViewColumn.One,
			{}
		);

		function updateMemoryInsights() {
			const pythonProcess = spawn('python', ['monitor_memory.py']);
			pythonProcess.stdout.on('data', (data) => {
				const memoryData = JSON.parse(data.toString());
				const htmlContent = `
                    <html>
                    <body>
                        <h1>Memory Insights</h1>
                        <h2>Virtual Memory</h2>
                        <ul>
                            ${Object.entries(memoryData["Virtual Memory"]).map(
					([key, value]) => `<li>${key}: ${value}</li>`
				).join('')}
                        </ul>
                        <h2>Swap Memory</h2>
                        <ul>
                            ${Object.entries(memoryData["Swap Memory"]).map(
					([key, value]) => `<li>${key}: ${value}</li>`
				).join('')}
                        </ul>
                        <h2>Top Memory-Consuming Processes</h2>
                        <table border="1">
                            <tr>
                                <th>PID</th>
                                <th>Name</th>
                                <th>Memory Used</th>
                            </tr>
                            ${memoryData["Top Memory Processes"].map(
					(proc) => `
                                    <tr>
                                        <td>${proc.PID}</td>
                                        <td>${proc.Name}</td>
                                        <td>${proc["Memory Used"]}</td>
                                    </tr>
                                `
				).join('')}
                        </table>
                    </body>
                    </html>
                `;
				panel.webview.html = htmlContent;
			});

			pythonProcess.stderr.on('data', (data) => {
				vscode.window.showErrorMessage(`Error: ${data}`);
			});
		}

		updateMemoryInsights();
		setInterval(updateMemoryInsights, 5000); // Refresh every 5 seconds
	});

	context.subscriptions.push(disposable);
}

function deactivate() { }

module.exports = { activate, deactivate };
