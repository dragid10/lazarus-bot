import pytest
from mockito import when, verify

from db.file_db import FileDB


@pytest.fixture()
def thread_id() -> str:
    return "967123350037745184"


@pytest.fixture()
def server_id() -> str:
    return "724940542933364768"


@pytest.fixture(scope="function")
def mock_db() -> FileDB:
    return FileDB()


def test_connect(mock_db):
    when(mock_db)._connect(...)
    mock_db._connect(options={"mode": "r+"})
    verify(mock_db, times=1)._connect(...)


def test_disconnect(mock_db):
    when(mock_db)._disconnect(...)
    mock_db._disconnect()
    verify(mock_db, times=1)._disconnect(...)


def test_add_thread_to_watchlist(mock_db, thread_id, server_id):
    when(mock_db).add_thread_to_watchlist(thread_id=thread_id, server_id=server_id)
    mock_db.add_thread_to_watchlist(thread_id=thread_id, server_id=server_id)
    verify(mock_db, times=1).add_thread_to_watchlist(...)


def test_remove_thread_from_watchlist(mock_db, thread_id, server_id):
    when(mock_db).remove_thread_from_watchlist(thread_id=thread_id, server_id=server_id)
    mock_db.remove_thread_from_watchlist(thread_id=thread_id, server_id=server_id)
    verify(mock_db, times=1).remove_thread_from_watchlist(...)


def test_thread_in_watchlist_is_true(mock_db, thread_id, server_id):
    expected = True
    when(mock_db).thread_in_watchlist(thread_id=thread_id, server_id=server_id).thenReturn(expected)
    actual = mock_db.thread_in_watchlist(thread_id=thread_id, server_id=server_id)
    assert actual is expected


def test_thread_in_watchlist_is_false(mock_db, thread_id, server_id):
    expected = False
    when(mock_db).thread_in_watchlist(thread_id=thread_id, server_id=server_id).thenReturn(expected)
    actual = mock_db.thread_in_watchlist(thread_id=thread_id, server_id=server_id)
    assert actual is expected
