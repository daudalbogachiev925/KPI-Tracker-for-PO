import json

def load(path="okrs.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def progress(kr):
    target = kr["target"]
    current = kr["current"]
    start = kr.get("start", 0)
    if target == start:
        return 0
    p = (current - start) / (target - start)
    return max(0, min(1, p))
