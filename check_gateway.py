def check_gateway(facts):
    if facts.get("IP정상") is True and facts.get("Gateway핑성공") is False:
        return "R8"
    if facts.get("Gateway외부핑성공") is True and facts.get("외부IP핑성공") is False:
        return "R9"
    return None