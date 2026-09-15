RULES = {
    "R1": {"cause": "케이블 분리 또는 NIC 문제", "action": "케이블/링크 상태 확인"},
}

def check_ip(facts): # 여윤우
    if facts.get("IP없음") or facts.get("IP주소") == "169.254":
        return "R5"
    if facts.get("IP중복"):
        return "R6"
    if facts.get("서브넷오류"):
        return "R7"
    return None