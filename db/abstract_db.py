from abc import ABC, abstractmethod


class AbstractDB(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _connect(self, username: str, password: str, hostname: str, port: int, options: dict = None):
        pass

    @abstractmethod
    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        pass

    @abstractmethod
    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        pass

    @abstractmethod
    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        pass
