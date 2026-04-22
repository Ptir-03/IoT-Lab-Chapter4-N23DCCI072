import matplotlib
matplotlib.use('Agg')  # Lệnh quan trọng để vẽ biểu đồ không cần giao diện đồ họa
import matplotlib.pyplot as plt
import csv

temps, hums, dists = [], [], []

# Đọc dữ liệu từ file CSV
with open('wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row['temperature']))
        hums.append(float(row['humidity']))
        dists.append(float(row['distance']))

# Vẽ dashboard với 3 subplot
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Biểu đồ Nhiệt độ (Đỏ)
axes[0].plot(temps, 'r-')
axes[0].axhline(y=30, color='orange', linestyle='--')
axes[0].set_ylabel('Temp (C)')
axes[0].set_title('Server Room Dashboard')

# Biểu đồ Độ ẩm (Xanh dương)
axes[1].plot(hums, 'b-')
axes[1].axhline(y=80, color='orange', linestyle='--')
axes[1].set_ylabel('Humidity (%)')

# Biểu đồ Khoảng cách (Xanh lá)
axes[2].plot(dists, 'g-')
axes[2].axhline(y=30, color='red', linestyle='--')
axes[2].set_ylabel('Distance (cm)')
axes[2].set_xlabel('Sample')

plt.tight_layout()
plt.savefig('server_dashboard.png', dpi=150)
print('Saved: server_dashboard.png')
