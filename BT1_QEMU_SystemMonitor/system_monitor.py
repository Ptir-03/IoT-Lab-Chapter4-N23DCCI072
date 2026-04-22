import psutil
import time
from datetime import datetime

# Đường dẫn file log
LOG_FILE = "system_monitor.log"

def monitor_system():
    with open(LOG_FILE, "a") as log_file:
        while True:
            # Thu thập dữ liệu
            cpu_avg = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            ram_used_mb = ram.used // (1024 * 1024)
            ram_total_mb = ram.total // (1024 * 1024)
            ram_pct = ram.percent
            disk_pct = psutil.disk_usage('/').percent
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Xác định trạng thái cảnh báo
            if cpu_avg > 80 or ram_pct > 80:
                status = "CRITICAL"
            elif cpu_avg > 50 or ram_pct > 50:
                status = "WARNING"
            else:
                status = "OK"

            # Ngắt dòng log để tránh lỗi E501 (dòng quá dài)
            log_entry = f"[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB " \
                        f"({ram_pct}%) | Disk: {disk_pct}% | {status}"

            print(log_entry)
            log_file.write(log_entry + "\n")
            log_file.flush()  # Đảm bảo dữ liệu được ghi ngay lập tức
            time.sleep(1)

if __name__ == "__main__":
    print("He thong dang giam sat... Nhan Ctrl+C de dung.")
    try:
        monitor_system()
    except KeyboardInterrupt:
        print("\nDa dung giam sat.")
