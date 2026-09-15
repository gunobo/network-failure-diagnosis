def check_perfomance(facts):
    if facts.get("연결성공") is True and fact.get("응답느림") is True and fact.get("RTT높음"):
        return "R15"
    if facts.get("패킷손실률높음") is True:
        return "R16"
    if facts.get("웹느림") is True and facts.get("모바일데이터정상") is True:
        return "R17"
    return None