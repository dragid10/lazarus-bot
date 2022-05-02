import redis as redis

from db.abstract_db import AbstractDB
from util import logger, config

logger = logger.get_logger()


class RedisDB(AbstractDB):
    def __init__(self):
        super().__init__()
        self._watchlist: redis.Redis = None
        self._connect(config.redis_user, config.redis_pass, config.redis_host, config.redis_port, {})

    def _connect(self, username: str, password: str, hostname: str, port: int, options: dict = None):
        self._watchlist: redis.Redis = redis.StrictRedis(host=config.redis_host,
                                                         port=config.redis_port,
                                                         db=0,
                                                         password=config.redis_pass,
                                                         decode_responses=True,
                                                         socket_keepalive=True,
                                                         retry_on_timeout=True, )
        self._watchlist.ping()

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        self._watchlist.set(server_id, thread_id)

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        self._watchlist.delete(server_id)

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        if not thread_id:
            return False
        if not server_id:
            return False
        if not self._watchlist:
            return False

        channel_watchlists = self._watchlist.get(server_id, )
        if not channel_watchlists:
            return False

        if thread_id in channel_watchlists:
            return True
