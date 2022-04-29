import pytest


@pytest.fixture
def keepalive_on_cmd():
    pass


@pytest.fixture
async def keepalive_off_cmd():
    pass


@pytest.fixture
async def archival_event():
    pass


def test_on_thread_update_keepalive_off(when, keepalive_off_cmd):
    assert False
