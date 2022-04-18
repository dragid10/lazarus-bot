from discord import Thread
from icecream import ic


def null_or_empty(input: str) -> bool:
    return input is None or input.casefold().strip() == ""


def is_thread(channel) -> bool:
    return isinstance(channel, Thread)


def thread_archive_event(pre_payload, post_payload) -> bool:
    if is_thread(pre_payload) and is_thread(post_payload):
        ic(f"A thread related event occurred")
        return not pre_payload.archived and post_payload.archived
    return False
