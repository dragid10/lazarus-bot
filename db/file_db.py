import json

from db.db_impl import AbstractDB
from util import logger

logger = logger.get_logger()


class FileDB(AbstractDB):
    def __init__(self):
        super().__init__()
        tmp_dict = {}
        self.db_file = open("lazarus-db.json", mode="w+")
        json.dump(tmp_dict, self.db_file, indent=3)
        self.db_file.close()
        self._watchlist = {}

    def connect(self, username: str = None, password: str = None, hostname: str = None, port: int = None, options: dict = {"mode": "r+"},):
        self.db_file = open("lazarus-db.json", mode=options["mode"])
        try:
            self._watchlist = json.load(self.db_file)
        except Exception as e:
            logger.error(f"Couldn't open file???: {e}")

    def disconnect(self):
        json.dump(self._watchlist, self.db_file, indent=3)
        self.db_file.close()

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        self._watchlist[server_id] = []
        self._watchlist[server_id].append(thread_id)
        self.db_file.seek(0)
        self.db_file.truncate()
        self.disconnect()

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        if self.thread_in_watchlist(thread_id, server_id):
            self._watchlist.get(server_id, []).remove(thread_id)
        self.db_file.seek(0)
        self.db_file.truncate()
        self.disconnect()

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        resp = thread_id in self._watchlist.get(server_id, [])
        return resp
