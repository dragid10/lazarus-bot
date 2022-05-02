from collections import defaultdict

from db.abstract_db import AbstractDB
from util import logger

logger = logger.get_logger()


class InMemoryDB(AbstractDB):
    def __init__(self):
        super().__init__()
        self.__watchlist = defaultdict(set[str])

    def _connect(self, username: str, password: str, hostname: str, port: int, options: dict = None):
        pass

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist[server_id].add(thread_id)

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist[server_id].discard(thread_id)

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        resp = thread_id in self.__watchlist[server_id]
        return resp