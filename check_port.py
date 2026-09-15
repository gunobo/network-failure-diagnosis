"""
R13. IF 인터넷(도메인 접속)은 정상 AND 특정 서비스(포트)만 접속 실패
     THEN 원인 = 방화벽 차단 또는 해당 서비스 다운

R14. IF 특정 사이트만 안 열림 AND 다른 브라우저/시크릿모드에서도 동일
     THEN 원인 = 방화벽/보안 프로그램 차단
"""
def check_port(facts):
    if facts.get("인터넷") == "정상" and facts.get("특정 서비스") == "접속 실패":
        return "R1"
    if facts.get("특정PC만안됨"):
        return "R2"
    return None