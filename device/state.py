from enum import Enum


class AssistantState(Enum):
    # Idle constant commands while waiting for the answer
    IDLE = "idle"
    WAITING_FOR_HELP_CONFIRMATION = "waiting_for_help_confirmation"