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

def generate_statistics(records_dir):
    total_records = 0

    info_count = 0
    warning_count = 0
    error_count = 0
    errors_by_module = {}

    for file_name, records in records_dir.items():

        total_records += len(records)
        
        for record in records:

            if record["level"] == "INFO":
                info_count += 1

            elif record["level"] == "WARNING":
                warning_count += 1

            elif record["level"] == "ERROR":
                error_count += 1
                module = record["module"]

                if module in errors_by_module:
                    errors_by_module[module] += 1
                else:
                    errors_by_module[module] = 1

    statistics = {
        "total_records": total_records,
        "INFO": info_count,
        "WARNING": warning_count,
        "ERROR": error_count,
        "errors_by_module": errors_by_module
    }

    return statistics


result = log_files()
status = generate_statistics(result)
print(status)


