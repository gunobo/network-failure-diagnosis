"""
네트워크 장애 진단 전문가 시스템
IF-THEN 규칙 기반 (R1~R19)
"""

"""
- check_physical : 임제민
- check_ip 함수 : 여윤우
- check_gateway 함수 : 박범호
- check_dns 함수 : 김현우
- check_port 함수 : 임제민
- check_performance 함수 : 박범호
"""

import check_physical
import check_port
import check_ip
import check_gateway
import check_dns
import check_performance

RULES = {}
RULES.update(check_physical.RULES)
RULES.update(check_ip.RULES)
RULES.update(check_gateway.RULES)
RULES.update(check_dns.RULES)
RULES.update(check_port.RULES)
RULES.update(check_performance.RULES)

CHECK_ORDER = [check_physical, check_ip, check_gateway, check_dns, check_port, check_performance]
def diagnose(facts: dict):
    """
    추론 엔진 본체.
    facts: 입력된 사실 딕셔너리
    반환: (rule_id, rule_info, log)
    """
    log = []
    for check_func in CHECK_ORDER:
        log.append(check_func.check)
        rule_id = check_func(facts)
        if rule_id:
            return rule_id, RULES[rule_id], log
 
    if facts.get("인터넷정상"):
        return "R18", RULES["R18"], log
    return "R19", RULES["R19"], log

test_cases = [
    {
        "name": "예시1 - DNS 문제",
        "facts": {
            "연결표시": "정상",
            "IP주소": "192.168.0.10",
            "게이트웨이핑": "성공",
            "외부IP핑": "성공",
            "도메인핑": "실패",
        }
    },
    {
        "name": "예시2 - 방화벽/포트 문제",
        "facts": {
            "연결표시": "정상",
            "IP주소": "192.168.0.10",
            "게이트웨이핑": "성공",
            "외부IP핑": "성공",
            "도메인핑": "성공",
            "인터넷정상": True,
            "특정서비스실패": True,
        }
    },
    {
        "name": "예시3 - DHCP 문제",
        "facts": {
            "연결표시": "정상",
            "IP주소": "169.254.13.5",
        }
    },
]

for case in test_cases:
    result = diagnose(case["facts"])
    print(f"[{case['name']}]")
    print(f"  입력 사실: {case['facts']}")
    print(f"  적용 규칙: {result['rule']}")
    print(f"  진단 원인: {result['cause']}")
    print(f"  권장 조치: {result['action']}")
    print()