import psutil
import os

def get_system_stats():
    disk_path = 'C:\\' if os.name == 'nt' else '/'
    
    battery = psutil.sensors_battery()
    battery_percent = round(battery.percent, 1) if battery else "N/A (Cloud)"

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            info = proc.info
            if info['memory_percent'] is not None:
                processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    top_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]

    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage(disk_path).percent,
        "battery": battery_percent,
        "top_processes": top_processes
    }
