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
        ic(self.db_file.readlines())

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


@pytest.fixture()
def thread_id() -> str:
    return "967123350037745184"


@pytest.fixture()
def server_id() -> str:
    return "724940542933364768"


@pytest.fixture(scope="function")
def db() -> FileDB:
    file_db = MockFileDB()
    return file_db


def test_connect(db):
    db.connect(options={"mode": "r+"})
    assert db


def test_disconnect(db):
    db.disconnect()
    assert not db.db_file


def test_add_thread_to_watchlist(db, thread_id, server_id):
    db.add_thread_to_watchlist(thread_id, server_id)
    assert len(db._watchlist) > 0
