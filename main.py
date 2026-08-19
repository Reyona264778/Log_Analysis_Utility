# from sample_logs import *
import os

def log_files():
    records_dir = {}
    files = os.listdir("sample_logs")
    for file in files:
        
        if file.endswith(".log"):  
            records = parse_line(file)
            records_dir[file] = records
        else:
            print(f"Warning!, Non-log file found : {file}")
    return records_dir


def parse_line(file_name):
    record = []
    try:
        filepath = os.path.join("sample_logs",file_name)
        with open(filepath, "r") as file:
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
        print("Log File not found")
    return record

result = log_files()
print(result)