from discord import Thread

from util import logger

logger = logger.get_logger()


def null_or_empty(input: str) -> bool:
    return input is None or input.casefold().strip() == ""


def is_thread(channel) -> bool:
    logger.debug(type(channel))
    return isinstance(channel, Thread)


def thread_archive_event(pre_payload, post_payload) -> bool:
    if is_thread(pre_payload) and is_thread(post_payload):
        logger.debug(f"A thread related event occurred")
        return not pre_payload.archived and post_payload.archived
    return False
