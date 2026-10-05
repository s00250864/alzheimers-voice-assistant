from device.commands import understand_command
from device.assistant import Assistant
from device.state import AssistantState


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


def test_assistant_starts_idle():
    assistant = Assistant()

    assert assistant.state == AssistantState.IDLE


def test_help_changes_state():
    assistant = Assistant()

    assistant.process_command("help me")

    assert assistant.state == AssistantState.WAITING_FOR_HELP_CONFIRMATION


def test_help_confirmation_yes():
    assistant = Assistant()

    assistant.process_command("help me")

    response = assistant.process_command("yes")

    assert response == "I am contacting your emergency contact."
    assert assistant.state == AssistantState.IDLE


def test_help_confirmation_no():
    assistant = Assistant()

    assistant.process_command("help me")

    response = assistant.process_command("no")

    assert response == "Okay. I will not contact them."
    assert assistant.state == AssistantState.IDLE

def test_unknown_help_confirmation_does_not_trigger_contact():
    assistant = Assistant()

    assistant.process_command("help me")

    response = assistant.process_command("banana")

    assert response == "Sorry, I did not understand. Please say yes or no."

    assert assistant.state == AssistantState.WAITING_FOR_HELP_CONFIRMATION