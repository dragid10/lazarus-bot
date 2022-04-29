import io
import json

import pytest
from icecream import ic

from db.file_db import FileDB


class MockFileDB(FileDB):
    def __init__(self):
        super().__init__()
        tmp_dict = {}
        self.db_file = io.StringIO(json.dumps(tmp_dict))
        self.db_file.close()
        self._watchlist = {}

    def connect(self, username: str = None, password: str = None, hostname: str = None, port: int = None, options: dict = None, ):
        self.db_file = io.StringIO("{}")
        try:
            self._watchlist = json.loads(self.db_file.read())
            ic(self._watchlist)
        except Exception as e:
            ic(f"Couldn't open file???: {e}")

    def disconnect(self):
        self.db_file = io.StringIO(json.dumps(self._watchlist))
        ic(self.db_file.readlines())

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        self._watchlist[server_id] = []
        self._watchlist[server_id].append(thread_id)
        self.db_file.truncate()
        self.disconnect()

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        if self.thread_in_watchlist(thread_id, server_id):
            self._watchlist.get(server_id, []).remove(thread_id)
        self.db_file.truncate()
        self.disconnect()

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        if not self.db_file or self.db_file.closed:
            self.connect(None, None, None, options={"mode": "r+"})
        resp = thread_id in self._watchlist.get(server_id, [])
        return resp


@pytest.fixture()
def thread_id() -> str:
    return "967123350037745184"


@pytest.fixture()
def server_id() -> str:
    return "724940542933364768"


@pytest.fixture(scope="function")
def db() -> MockFileDB:
    file_db = MockFileDB()
    return file_db


def test_connect(db):
    db.connect(options={"mode": "r+"})
    assert db


def test_disconnect(db):
    db.disconnect()
    assert db.db_file.readlines() is not None


def test_add_thread_to_watchlist(db, thread_id, server_id):
    db.add_thread_to_watchlist(thread_id, server_id)
    assert len(db._watchlist[server_id]) > 0


def test_remove_thread_from_watchlist(db, thread_id, server_id):
    db.add_thread_to_watchlist(thread_id, server_id)
    assert len(db._watchlist[server_id]) > 0

    db.remove_thread_from_watchlist(thread_id, server_id)
    assert len(db._watchlist[server_id]) == 0


def test_thread_in_watchlist(db, thread_id, server_id):
    expected = False
    actual = db.thread_in_watchlist(thread_id, server_id)
    assert actual is expected
