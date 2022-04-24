import pytest

from db.memory_db import InMemoryDB


@pytest.fixture
def empty_watchlist():
    return InMemoryDB()


@pytest.fixture
def nonempty_watchlist(empty_watchlist, thread_id, server_id):
    watchlist = empty_watchlist
    watchlist.add_thread_to_watchlist(thread_id, server_id)
    return watchlist


@pytest.fixture()
def thread_id() -> str:
    return "967123350037745184"


@pytest.fixture()
def server_id() -> str:
    return "724940542933364768"


def test_connect():
    assert True


def test_add_thread_to_watchlist(empty_watchlist, thread_id, server_id):
    empty_watchlist.add_thread_to_watchlist(thread_id, server_id)
    assert empty_watchlist.thread_in_watchlist(thread_id, server_id)


def test_remove_thread_from_watchlist(nonempty_watchlist, thread_id, server_id):
    nonempty_watchlist.remove_thread_from_watchlist(thread_id, server_id)
    assert not nonempty_watchlist.thread_in_watchlist(thread_id, server_id)
