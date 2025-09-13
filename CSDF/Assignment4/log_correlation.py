import datetime
import re

# File paths
log_file1 = "server1.log"
log_file2 = "server2.log"

# Function to read log file and return list of lines
def read_log_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

# Function to parse log entries into structured data
def parse_logs(log_lines):
    log_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
    parsed_logs = []
    for log in log_lines:
        log = log.strip()
        match = re.match(log_pattern, log)
        if match:
            timestamp = datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
            level = match.group(2)
            message = match.group(3)
            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return parsed_logs

# Read actual log files
logs1 = read_log_file(log_file1)
logs2 = read_log_file(log_file2)

# Parse logs
parsed_logs1 = parse_logs(logs1)
parsed_logs2 = parse_logs(logs2)

# Event correlation: same WARNING message within 10 seconds
correlated_events = []
for log1 in parsed_logs1:
    for log2 in parsed_logs2:
        time_diff = abs((log1["timestamp"] - log2["timestamp"]).total_seconds())
        if log1["level"] == "WARNING" and log2["level"] == "WARNING" and log1["message"] == log2["message"] and time_diff <= 10:
            correlated_events.append((log1, log2))

# Display correlated events
print("Correlated Events:")
for e1, e2 in correlated_events:
    print(f"{e1['timestamp']} | {e1['level']} | {e1['message']} <--> {e2['timestamp']} | {e2['level']} | {e2['message']}")
