# ⚡ Live System Health Monitor

A real-time server and system resource monitoring web dashboard built with **Python (Flask)**, **`psutil`**, and **Chart.js**[cite: 12]. Deployed live on **Render** to visualize CPU, RAM, Disk usage, System Uptime, and top memory-consuming processes in real time[cite: 12].

🔗 **Live Demo:** [https://system-health-monitor-lfjf.onrender.com](https://system-health-monitor-lfjf.onrender.com)[cite: 1, 2]

---

## ✨ Key Features

- **Real-Time Telemetry:** Auto-refreshes every 2 seconds via a REST API (`/api/stats`) without page reloads[cite: 3].
- **Interactive Area Chart:** Smooth, dual-axis live line/area visualization tracking CPU % and RAM % trends using Chart.js[cite: 12].
- **Cross-Platform Disk & Power Detection:** Automatically detects Windows (`C:\`) and Linux (`/`) root filesystems (`os.name`) and adapts battery status for cloud server environments (`Cloud Server`)[cite: 5, 12].
- **System Uptime & OS Telemetry:** Displays continuous server uptime (`days, hours, minutes`) and host OS architecture (`Linux x86_64`)[cite: 12].
- **Threshold Alerts & Controls:** Highlights critical usage (`> 80%`) in red, triggers a high-resource warning banner (`> 85%`), and includes a **Pause / Resume** stream toggle[cite: 10, 12].
- **Top 5 Process Tracker:** Lists the top 5 memory-consuming processes with PID, process name, and visual RAM usage bars.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, `psutil`[cite: 1, 5]
- **Frontend:** HTML5, CSS3 (Responsive Grid), Vanilla JavaScript (Fetch API), Chart.js
- **Deployment:** GitHub + Render Cloud Web Service[cite: 1, 7]

---

## 🚀 Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vaishnavij2917-spec/system-health-monitor.git](https://github.com/vaishnavij2917-spec/system-health-monitor.git)
   cd system-health-monitor
