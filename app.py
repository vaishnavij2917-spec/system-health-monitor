from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('C:\\')
    battery = psutil.sensors_battery()
    
    # Top 5 RAM consuming apps
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    top_processes = sorted(processes, key=lambda p: p['memory_percent'] or 0, reverse=True)[:5]

    return jsonify({
        'cpu': cpu,
        'ram_percent': memory.percent,
        'ram_used': round(memory.used / (1024**3), 2),
        'ram_total': round(memory.total / (1024**3), 2),
        'disk_percent': disk.percent,
        'battery': battery.percent if battery else "N/A",
        'plugged': battery.power_plugged if battery else False,
        'top_processes': top_processes
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    