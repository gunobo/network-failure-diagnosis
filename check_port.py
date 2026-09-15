RULES = {
    "R13": {"cause": "방화벽 차단 또는 해당 서비스 다운", "action": "방화벽 포트 확인, 서비스 상태 확인"},
    "R14": {"cause": "방화벽/보안 프로그램 차단", "action": "방화벽/보안앱 예외 설정 확인"},
}

def check_port(facts):
    internet_ok = facts.get("인터넷정상")
    specific_service_fail = facts.get("특정서비스실패")
    site_fail_other_browser = facts.get("타브라우저도실패")
 
    if internet_ok and specific_service_fail:
        return "R13"
    if site_fail_other_browser:
        return "R14"
    return None