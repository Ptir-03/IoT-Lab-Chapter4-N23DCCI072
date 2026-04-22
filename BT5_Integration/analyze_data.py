import csv

temps, hums, dists = [], [], []
warnings = 0
intrusions = 0  # distance < 30cm

with open('wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = float(row['temperature'])
        h = float(row['humidity'])
        d = float(row['distance'])
        temps.append(t)
        hums.append(h)
        dists.append(d)
        if row['status'] != 'NORMAL':
            warnings += 1
        if d < 30:
            intrusions += 1

print('=== BÁO CÁO PHÒNG SERVER ===')
print(f'Tổng mẫu: {len(temps)}')
print(f'Nhiệt độ: TB={sum(temps)/len(temps):.1f}C, Min={min(temps):.1f}, Max={max(temps):.1f}')
print(f'Phát hiện người vào: {intrusions} lần')
print(f'Cảnh báo: {warnings}/{len(temps)} ({warnings/len(temps)*100:.0f}%)')

# Ghi report
with open('report.txt', 'w') as f:
    f.write(f'Tong mau: {len(temps)}\n')
    f.write(f'Nhiet do TB: {sum(temps)/len(temps):.1f}\n')
    f.write(f'Phat hien nguoi: {intrusions}\n')
