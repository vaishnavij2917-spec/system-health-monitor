from flask import Flask, jsonify, render_template
import psutil
import platform
import time
import os

app = Flask(__name__)

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)
    days, rem = divmod(uptime_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, _ = divmod(rem, 60)
    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    return f"{hours}h {minutes}m"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk_path = 'C:\\' if os.name == 'nt' else '/'
    disk = psutil.disk_usage(disk_path)
    battery = psutil.sensors_battery()
    
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
        'disk_used': round(disk.used / (1024**3), 1),
        'disk_total': round(disk.total / (1024**3), 1),
        'battery': battery.percent if battery else "N/A",
        'plugged': battery.power_plugged if battery else False,
        'uptime': get_uptime(),
        'os_info': f"{platform.system()} ({platform.machine()})",
        'top_processes': top_processes
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
