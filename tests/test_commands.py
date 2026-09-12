from device.commands import understand_command


def test_time_command():
    result = understand_command("what time is it")

    assert result == "TIME"


def test_find_phone_command():
    result = understand_command("find my phone")

    assert result == "FIND_PHONE"


def test_help_command():
    result = understand_command("help me")

    assert result == "HELP"


def test_unknown_command():
    result = understand_command("make me a sandwich")

    assert result == "UNKNOWN"


def test_time_command_with_longer_sentence():
    assert understand_command("can you please tell me the time") == "TIME"


def test_find_phone_is_case_insensitive():
    assert understand_command("FIND MY PHONE") == "FIND_PHONE"


def test_help_command_is_case_insensitive():
    assert understand_command("HELP ME") == "HELP"