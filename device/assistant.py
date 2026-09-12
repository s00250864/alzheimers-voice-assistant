from datetime import datetime

from device.commands import understand_command


def tell_time() -> str:
    current_time = datetime.now().strftime("%H:%M")

    return f"The current time is {current_time}."


def find_phone() -> str:
    # For now this is only simulated.
    # Later this function will contact our server.
    return "I am finding your phone."


def request_help() -> str:
    # Do not contact anyone yet.
    # Eventually this will trigger the emergency-contact workflow.
    return "Do you want me to contact your emergency contact?"


def process_command(command: str) -> str:
    intent = understand_command(command)

    if intent == "TIME":
        return tell_time()

    if intent == "FIND_PHONE":
        return find_phone()

    if intent == "HELP":
        return request_help()

    return "Sorry, I did not understand that command."


def main():
    print("Voice Assistant")
    print("Type 'exit' to stop.\n")

    while True:
        command = input("You: ")

        if command.lower() == "exit":
            print("Assistant: Goodbye.")
            break

        response = process_command(command)

        print(f"Assistant: {response}")


if __name__ == "__main__":
    main()