import pytest
from discord import Thread, ApplicationContext, Guild
from mockito import verify, mock, ANY
from mockito.mocking import _Dummy

from bots import lazarus
from db.abstract_db import AbstractDB
from db.file_db import FileDB
from db.memory_db import InMemoryDB
from db.redis_db import RedisDB


@pytest.mark.asyncio
async def mock_return(opt=None):
    return mock()


@pytest.fixture
def pre_thread_archive():
    mock_thread = {
        "guild": mock({"id": 1234}, spec=Guild),
        "id": 5678,
        "archived": False,
    }
    mock_obj = mock(mock_thread, spec=Thread)
    mock_obj.unarchive = mock_return
    mock_obj.send = mock_return
    return mock_obj


@pytest.fixture
def post_thread_archive():
    mock_thread = {
        "guild": mock({"id": 1234}, spec=Guild),
        "id": 5678,
        "archived": True,
    }
    mock_obj = mock(mock_thread, spec=Thread)
    mock_obj.unarchive = mock_return
    mock_obj.send = mock_return
    return mock_obj


@pytest.fixture
def context():
    mock_context = {
        "channel": mock({
            "guild": mock({"id": 1234}, spec=Guild),
            "id": 5678,
            "archived": True
        }, spec=Thread),
        "guild_id": 1234,
        "id": 4321,
    }
    mock_obj = mock(mock_context, spec=ApplicationContext)
    mock_obj.respond = mock_return
    mock_obj.send_response = mock_return
    return mock_obj


@pytest.fixture
def lazarus_bot(db):
    lazarus.set_db_source(db)
    return lazarus


@pytest.fixture
def db():
    return AbstractDB


@pytest.mark.asyncio
async def test_on_ready(when, lazarus_bot):
    when(lazarus_bot).on_ready().thenAnswer(mock_return)
    await lazarus_bot.on_ready()
    verify(lazarus_bot, times=1).on_ready()


@pytest.mark.asyncio
async def test_on_thread_update_watched_thread(when, lazarus_bot, pre_thread_archive, post_thread_archive):
    # Patch inner db obj to ensure that the function was called
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(True)
    await lazarus_bot.on_thread_update(pre_thread_archive, post_thread_archive)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")


@pytest.mark.asyncio
async def test_on_thread_update_unwatched_thread(when, lazarus_bot, pre_thread_archive, post_thread_archive):
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(False)
    await lazarus_bot.on_thread_update(pre_thread_archive, post_thread_archive)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")


@pytest.mark.asyncio
async def test_ping(when, lazarus_bot, context):
    await lazarus_bot.ping(context)


@pytest.mark.asyncio
async def test_keepalive_on_watched_thread(when, lazarus_bot, context):
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(True)
    await lazarus_bot.keepalive_on(context)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")


@pytest.mark.asyncio
async def test_keepalive_on_unwatched_thread(when, lazarus_bot, context):
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(False)
    when(lazarus_bot.db).add_thread_to_watchlist(ANY(str), ANY(str))
    await lazarus_bot.keepalive_on(context)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")
    verify(lazarus_bot.db, times=1).add_thread_to_watchlist("5678", "1234")


@pytest.mark.asyncio
async def test_keepalive_off_watched_thread(when, lazarus_bot, context):
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(True)
    when(lazarus_bot.db).remove_thread_from_watchlist(ANY(str), ANY(str))
    await lazarus_bot.keepalive_off(context)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")
    verify(lazarus_bot.db, times=1).remove_thread_from_watchlist("5678", "1234")


@pytest.mark.asyncio
async def test_keepalive_off_unwatched_thread(when, lazarus_bot, context):
    when(lazarus_bot.db).thread_in_watchlist(ANY(str), ANY(str)).thenReturn(False)
    await lazarus_bot.keepalive_off(context)
    verify(lazarus_bot.db, times=1).thread_in_watchlist("5678", "1234")


def test_run(when, lazarus_bot):
    bot_obj = lazarus_bot.bot
    when(bot_obj).run(ANY(str), reconnect=ANY(bool))
    lazarus_bot.run()
    verify(bot_obj, times=1).run(...)


@pytest.mark.parametrize("input, expected", [("memory", mock(InMemoryDB)), ("local", mock(FileDB)), ("redis", mock(RedisDB))])
def test_db_mapper(when, lazarus_bot, input, expected):
    when(lazarus_bot).db_mapper(input).thenReturn(expected)
    actual = lazarus_bot.db_mapper(input)
    assert isinstance(actual, _Dummy)