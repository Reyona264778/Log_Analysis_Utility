from sample_logs import *

record = []
try:
    with open("sample_logs/log1.log", "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 5 :
                data = {
                            "timestamp" : f"{parts[0]} {parts[1]}",
                            "level" : parts[2],
                            "module" : parts[3].strip("[]"),
                            "msg" : " ".join(parts[4:]),
                            # parts_last[0] : parts_last[1],
                        }
                record.append(data)
            else:
                print(f"Malformed line skipped : {line.strip()}")
except FileNotFoundError:
    print("Log File nor found")
print(record)
    