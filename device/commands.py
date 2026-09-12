def understand_command(command: str) -> str:
    """
    Takes the user's command and determines what action
    the assistant should perform.
    """

    command = command.lower().strip()

    if "time" in command:
        return "TIME"

    if "find my phone" in command:
        return "FIND_PHONE"

    if "help me" in command:
        return "HELP"

    return "UNKNOWN"