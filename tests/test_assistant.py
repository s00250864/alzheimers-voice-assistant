from device.assistant import Assistant
from device.state import AssistantState


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