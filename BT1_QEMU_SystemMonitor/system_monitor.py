import psutil
import time
from datetime import datetime


LOG_FILE = "system_monitor.log"


def monitor_system():
    with open(LOG_FILE, "a") as log_file:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            ram_pct = ram.percent
            disk_pct = psutil.disk_usage('/').percent
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            status = "OK"
            if cpu > 80 or ram_pct > 80:
                status = "CRITICAL"
            elif cpu > 50 or ram_pct > 50:
                status = "WARNING"

            log_entry = f"[{now}] CPU:{cpu}% | RAM:{ram_pct}% | " \
                        f"Disk:{disk_pct}% | {status}"

            print(log_entry)
            log_file.write(log_entry + "\n")
            log_file.flush()
            time.sleep(1)


if __name__ == "__main__":
    try:
        monitor_system()
    except KeyboardInterrupt:
        print("\nStopped.")
