from collections import defaultdict

from db.abstract_db import AbstractDB
from util import logger

logger = logger.get_logger()


class InMemoryDB(AbstractDB):
    def __init__(self):
        super().__init__()
        self.__watchlist = defaultdict(list[str])

    def _connect(self, username: str, password: str, hostname: str, port: int, options: dict):
        pass

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist[server_id].append(thread_id)

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist[server_id].remove(thread_id)

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        return thread_id in self.__watchlist[server_id]
