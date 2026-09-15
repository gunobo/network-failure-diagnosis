RULES = {
    "R15": {
        "cause": "네트워크 혼잡 또는 대역폭 부족",
        "action": "대용량 다운로드 및 네트워크 사용량 확인",
    },
    "R16": {
        "cause": "회선 불안정 또는 장비 과부하",
        "action": "케이블 연결 상태, 회선 상태 및 네트워크 장비 부하 확인",
    },
    "R17": {
        "cause": "공유기 또는 로컬 네트워크 문제",
        "action": "공유기 상태 확인 및 같은 네트워크의 다른 기기에서 비교 테스트",
    },
}
def check(facts):
    if facts.get("연결성공") is True and facts.get("응답느림") is True and facts.get("RTT높음") is True:
        return "R15"
    if facts.get("패킷손실률높음") is True:
        return "R16"
    if facts.get("웹느림") is True and facts.get("모바일데이터정상") is True:
        return "R17"
    return None