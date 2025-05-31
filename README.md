# 🧠 Virtual Memory Simulator as VSCode Extension

A Visual Studio Code extension that provides real-time insights into system memory usage, including virtual memory, swap memory, and the top memory-consuming processes. Built using Python (`psutil`) and integrated seamlessly into VSCode using Node.js.

---

## 📦 Features

- Real-time **Virtual Memory** and **Swap Memory** stats  
- Live display of **Top 5 Memory-Consuming Processes**  
- Auto-refreshes every 5 seconds  
- Beautiful and interactive VSCode Webview interface  
- Lightweight and platform-independent  

---

## 📁 Project Structure

\`\`\`
.
├── extension.js           # Main VSCode extension script
├── monitor_memory.py      # Python backend for memory stats using psutil
├── package.json           # Extension manifest
└── README.md              # Project documentation
\`\`\`

---

## 🛠️ Installation

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/CallmeSharanya/Virtual-memory-simulator-as-VSCode-extension.git
cd Virtual-memory-simulator-as-VSCode-extension
\`\`\`

### 2. Install Python Dependencies

Make sure Python (>=3.6) is installed.

\`\`\`bash
pip install psutil
\`\`\`

### 3. Install and Launch in VSCode

* Open the project in **VSCode**
* Press \`F5\` to launch the extension in a new Extension Development Host

---

## 🚀 Usage

1. Open the Command Palette (\`Ctrl+Shift+P\` or \`Cmd+Shift+P\`)
2. Run: **\`Show Memory Insights\`**
3. A new panel will appear with real-time memory statistics and process usage
4. Stats auto-refresh every 5 seconds

---

## 🧠 How It Works

### \`monitor_memory.py\`

A Python script that uses \`psutil\` to fetch system memory stats:

* Virtual Memory: total, used, free, buffers, cached, etc.
* Swap Memory: total, used, free, percentage used
* Top 5 memory-consuming processes (PID, name, memory used)

### \`extension.js\`

A Node.js script registered with VSCode:

* Executes \`monitor_memory.py\` using \`child_process.spawn\`
* Parses JSON output
* Dynamically generates a Webview panel with HTML content
* Updates stats every 5 seconds

---

## 🔧 Requirements

* [Python](https://www.python.org/downloads/) 3.6 or later
* \`psutil\` Python package
* [Node.js](https://nodejs.org/)
* Visual Studio Code

---

## 🤝 Contributing

Contributions are welcome! Here’s how you can help:

* Fork the repo
* Create a feature branch (\`git checkout -b feature-name\`)
* Commit your changes (\`git commit -m "feat: add new feature"\`)
* Push to your branch (\`git push origin feature-name\`)
* Submit a Pull Request 🚀

---

## 🙋‍♀️ Author

**Sharanya** – [GitHub](https://github.com/CallmeSharanya)

---

## ⭐️ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!
