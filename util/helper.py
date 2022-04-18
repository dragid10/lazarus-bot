from discord import Thread


def null_or_empty(input: str) -> bool:
    return input is None or input.casefold().strip() == ""


def is_thread(channel) -> bool:
    return isinstance(channel, Thread)
