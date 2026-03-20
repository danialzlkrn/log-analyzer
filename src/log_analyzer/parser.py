import re
from datetime import datetime

LOG_PATTERN = r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) (?P<protocol>[^"]+)" (?P<status>\d{3}) (?P<size>\d+)'

def parse_line(line):
    match = re.match(LOG_PATTERN, line)
    if not match:
        return None

    data = match.groupdict()

    try:
        data["timestamp"] = datetime.strptime(data["timestamp"], "%d/%b/%Y:%H:%M:%S %z")

    except:
        data["timestamp"] = None

    data["status"] = int(data["status"])
    data["size"] = int(data["size"])

    return data


