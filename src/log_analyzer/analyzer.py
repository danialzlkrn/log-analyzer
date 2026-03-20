from collections import Counter
from parser import parse_line

def analyze_log(file_path):
    total = 0
    status_counter = Counter()
    ip_counter = Counter()
    path_counter = Counter()

    with open(file_path, "r") as f:
        for line in f:
            parsed = parse_line(line.strip())
            if not parsed:
                continue

            total += 1

            status = parsed["status"]
            ip = parsed["ip"]
            path = parsed["path"]

            if 200 <= status < 300:
                status_counter["2xx"] += 1
            elif 300 <= status < 400:
                status_counter["3xx"] += 1
            elif 400 <= status < 500:
                status_counter["4xx"] += 1
            elif 500 <= status < 600:
                status_counter["5xx"] += 1

            ip_counter[ip] += 1
            path_counter[path] += 1
    return {
        "total": total,
        "status": dict(status_counter),
        "top_ips": ip_counter.most_common(5),
        "top_paths": path_counter.most_common(5),
    }