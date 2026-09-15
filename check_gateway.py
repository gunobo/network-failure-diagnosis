RULES = {
    "R8": {"cause": "공유기 또는 LAN 자체 문제", "action": "공유기 전원, LAN 케이블 및 포트 연결 상태 확인"},
    "R9": {"cause": "라우팅 문제 또는 ISP 회선 장애", "action": "공유기 WAN 연결 및 라우팅 설정 확인, 통신사 장애 여부 확인"},
}

def check(facts):
    if facts.get("IP정상") is True and facts.get("Gateway핑성공") is False:
        return "R8"
    if facts.get("Gateway핑성공") is True and facts.get("외부IP핑성공") is False:
        return "R9"
    return None