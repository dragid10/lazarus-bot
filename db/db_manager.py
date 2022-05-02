from db.abstract_db import AbstractDB


class DBProvider:
    def __init__(self, db_impl: AbstractDB):
        self.db = db_impl

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        self.db.add_thread_to_watchlist(thread_id, server_id)

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        self.db.remove_thread_from_watchlist(thread_id, server_id)

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        return self.db.thread_in_watchlist(thread_id, server_id)