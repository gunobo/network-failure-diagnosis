RULES = {
    "R1": {"cause": "케이블 분리 또는 NIC 문제", "action": "케이블/링크 상태 확인"},
}

def check_physical(facts):
    if facts.get("연결표시") == "없음":
        return "R1"
    if facts.get("특정PC만안됨"):
        return "R2"
    return None

def check_ip(facts): # 여윤우
    return None

def check_gateway(facts): # 박범호
    return None

def check_dns(facts): # 김현우
    return None

def check_port(facts): # 임제민
    return None

def check_performance(facts): # 박범호
    return None

CHECK_ORDER = [check_physical, check_ip, check_gateway, check_dns, check_port, check_performance]
def diagnose(facts):
    log = []  # 어떤 함수를 거쳤는지 기록용 리스트
    for check_func in CHECK_ORDER:
        log.append(check_func.__name__)
        rule_id = check_func(facts)
        if rule_id:
            return rule_id, RULES[rule_id], log
    return "R19", RULES.get("R19", {"cause": "원인불명", "action": "로그 확인"}), log