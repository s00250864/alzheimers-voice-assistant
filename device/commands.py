def understand_command(command: str) -> str:
    command = command.lower().strip()

    time_phrases = [
        "time",
        "what time is it",
        "tell me the time",
        "current time",
        "tell me the time",
    ]

    phone_phrases = [
        "find my phone",
        "find my mobile",
        "ring my phone",
        "where is my phone",
    ]

    help_phrases = [
        "help me",
        "i need help",
        "get help",
        "i need assistance",
    ]

    for phrase in time_phrases:
        if phrase in command:
            return "TIME"

    for phrase in phone_phrases:
        if phrase in command:
            return "FIND_PHONE"

    for phrase in help_phrases:
        if phrase in command:
            return "HELP"

    return "UNKNOWN"