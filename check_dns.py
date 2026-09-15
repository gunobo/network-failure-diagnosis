RULES = {
    "R10" : {"cause" : "DNS 이름 해석 문제", "action": "DNS 이름 확인"},
    "R11" : {"cause" : "DNS 서버 다운 또는 설정 오류", "action" : "서버 재시작 및 설정 재확인"},
    "R12" : {"cause" : "DNS 서버 미응답", "action" : "서버 재요청"},
}

def check_dns(facts):
    if facts.get("목적지 IP로 ping") == "성공" and facts.get("목적지 도메인으로 ping") == "실패":
        return "R10"
    if facts.get("DNS서버 자체 ping") == "실패":
        return "R11"
    if facts.get("nslookup/dig 결과") == "응답 없음":
        return "R12"
    return None
    
