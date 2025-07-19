import csv, platform, psutil

with open("system_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Hostname", "OS", "CPU%", "Memory%", "Disk%"])
    writer.writerow([
        platform.node(),
        platform.platform(),
        psutil.cpu_percent(),
        psutil.virtual_memory().percent,
        psutil.disk_usage('/').percent
    ])
