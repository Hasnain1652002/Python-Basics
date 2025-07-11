import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

event_ids = {
    1102: 0, 4611: 0, 4624: 0, 4634: 0, 4648: 0, 4661: 0,
    4688: 0, 4698: 0, 4699: 0, 4702: 0, 4703: 0, 4719: 0,
    4798: 0, 4799: 0, 4985: 0, 5136: 0, 5140: 0, 5142: 0
}

log_file_name = r"d:\csv to csv\analysis_log_02_Jan_2020.txt"
output_dir = "CI5235_k1234567_FirstName/CI5235_logs/"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_log_file = os.path.join(output_dir, f"visdata_log_{timestamp}.txt")

os.makedirs(output_dir, exist_ok=True)

print("Processing log file...")

with open(log_file_name, "r") as file:
    for line in file:
        match = re.search(r"MATCHED Event ID:\s*(\d+)", line)
        if match:
            event_id = int(match.group(1))
            if event_id in event_ids:
                event_ids[event_id] += 1

print(event_ids)
print("Writing results to log file...")

with open(output_log_file, "w") as log_file:
    for event_id, count in event_ids.items():
        log_file.write(f"{event_id}: {count}\n")

event_id_list = []
event_count_list = []

print("Reading log file for visualization...")

with open(output_log_file, "r") as log_file:
    for line in log_file:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            event_id_list.append(parts[0])
            event_count_list.append(int(parts[1]))

print(event_id_list)
print(event_count_list)
print("Generating visualization...")

plt.figure(figsize=(10, 6))
plt.barh(event_id_list, event_count_list, color='skyblue')
plt.xlabel("Count")
plt.ylabel("Event ID")
plt.title("Event ID Occurrences in Log File")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

print("Script execution completed successfully.")
