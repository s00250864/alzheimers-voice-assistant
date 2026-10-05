from datetime import datetime

from device.commands import understand_command
from device.speech import speak
from device.state import AssistantState


class Assistant:

    def __init__(self):
        self.state = AssistantState.IDLE

    def tell_time(self) -> str:
        current_time = datetime.now().strftime("%H:%M")

        return f"The current time is {current_time}."

    def find_phone(self) -> str:
        # This will eventually contact our FastAPI server.
        return "I am finding your phone."

    def start_help_request(self) -> str:
        self.state = AssistantState.WAITING_FOR_HELP_CONFIRMATION

        return "Do you want me to contact your emergency contact?"

    def confirm_help_request(self, command: str) -> str:
        command = command.lower().strip()

        yes_answers = [
            "yes",
            "yeah",
            "yes please",
            "please do",
        ]

        no_answers = [
            "no",
            "no thanks",
            "cancel",
            "stop",
        ]

        if command in yes_answers:
            self.state = AssistantState.IDLE

            return "I am contacting your emergency contact."

        if command in no_answers:
            self.state = AssistantState.IDLE

            return "Okay. I will not contact them."

        return "Sorry, I did not understand. Please say yes or no."

    def process_command(self, command: str) -> str:

        # First check whether we're already in a conversation.
        if self.state == AssistantState.WAITING_FOR_HELP_CONFIRMATION:
            return self.confirm_help_request(command)

        # Otherwise interpret this as a new command.
        intent = understand_command(command)

        if intent == "TIME":
            return self.tell_time()

        if intent == "FIND_PHONE":
            return self.find_phone()

        if intent == "HELP":
            return self.start_help_request()

        return "Sorry, I did not understand that command."


def main():

    assistant = Assistant()

    print("Home Assistant")
    print("Type 'exit' to stop.\n")

    while True:

        command = input("You: ")

        if command.lower().strip() == "exit":
            response = "Goodbye."

            print(f"Assistant: {response}")
            speak(response)

            break

        response = assistant.process_command(command)

        print(f"Assistant: {response}")
        speak(response)


if __name__ == "__main__":
    main()