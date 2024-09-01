# ===== Logging Support Functions

def orchestrator_responder(response_code: int) -> str:
    return f"POST booking refresh, orchestrator returned status code: {response_code}"