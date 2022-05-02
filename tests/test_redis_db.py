import pytest
from mockito import ANY, verify, mock

from db.redis_db import RedisDB


@pytest.fixture
def mock_db():
    return mock(RedisDB)


def test_connect(when, mock_db):
    #  Stub connect method and make sure it gets called at least once
    when(mock_db)._connect(username=ANY(str), password=ANY(str), hostname=ANY(str), port=ANY(int))
    mock_db._connect(username="user", password="pass", hostname="abc123.com", port=1234, )
    verify(mock_db, times=1)._connect(username="user", password="pass", hostname="abc123.com", port=1234, )


def test_add_thread_to_watchlist(when, mock_db):
    when(mock_db).add_thread_to_watchlist(thread_id=ANY(str), server_id=ANY(str))
    mock_db.add_thread_to_watchlist(thread_id="1234", server_id="abcd")
    mock_db.add_thread_to_watchlist(thread_id="4567", server_id="efgh")
    verify(mock_db, times=2).add_thread_to_watchlist(...)


def test_remove_thread_from_watchlist(when, mock_db):
    when(mock_db).remove_thread_from_watchlist(thread_id=ANY(str), server_id=ANY(str))
    mock_db.remove_thread_from_watchlist(thread_id="4567", server_id="efgh")
    verify(mock_db, times=1).remove_thread_from_watchlist(...)


def test_thread_in_watchlist_is_true(when, mock_db):
    expected = True
    when(mock_db).thread_in_watchlist(thread_id="1234", server_id="abcd").thenReturn(expected)
    actual = mock_db.thread_in_watchlist(thread_id="1234", server_id="abcd")
    assert actual is expected


def test_thread_in_watchlist_is_false(when, mock_db):
    expected = False
    when(mock_db).thread_in_watchlist(thread_id="4321", server_id="dcba").thenReturn(expected)
    actual = mock_db.thread_in_watchlist(thread_id="4321", server_id="dcba")
    assert actual is expected