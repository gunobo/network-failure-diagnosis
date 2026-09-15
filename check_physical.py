RULES = {
    "R1": {"cause": "케이블 분리 또는 NIC 문제", "action": "케이블/링크 상태 확인"},
    "R2": {"cause": "해당 랜케이블 또는 NIC 불량", "action": "다른 포트/케이블로 테스트"},
    "R3": {"cause": "포트/케이블/장비 자체 문제", "action": "인터페이스 상태 확인"},
    "R4": {"cause": "케이블 접촉 불량 가능성", "action": "케이블 및 링크 상태 재확인"},
}

def check(facts):
    conn = facts.get("연결표시")
    same_pc_only = facts.get("특정PC만안됨")
    switch_port = facts.get("스위치포트상태")
 
    if conn == "없음":
        return "R1"
    if same_pc_only:
        return "R2"
    if switch_port == "Down":
        return "R3"
    if conn == "간헐적":
        return "R4"
    return None