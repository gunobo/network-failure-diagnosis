def check_physical(facts):
    if facts.get("연결표시") == "없음":
        return "R1"
    if facts.get("특정PC만안됨"):
        return "R2"
    return None