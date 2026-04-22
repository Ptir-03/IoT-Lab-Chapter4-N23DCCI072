import psutil
import time
from datetime import datetime


LOG_FILE = "system_monitor.log"


def monitor_system():
    with open(LOG_FILE, "a") as log_file:
        while True:
            c = psutil.cpu_percent(interval=1)
            r = psutil.virtual_memory().percent
            d = psutil.disk_usage('/').percent
            t = datetime.now().strftime("%H:%M:%S")
            s = "OK"
            if c > 80 or r > 80:
                s = "CRITICAL"
            elif c > 50 or r > 50:
                s = "WARNING"
            msg = f"[{t}] CPU:{c}% | RAM:{r}% | Disk:{d}% | {s}"
            print(msg)
            log_file.write(msg + "\n")
            log_file.flush()
            time.sleep(1)


if __name__ == "__main__":
    try:
        monitor_system()
    except KeyboardInterrupt:
        pass
