import redis as redis

from db.db_impl import AbstractDB
from util import logger, config

logger = logger.get_logger()


class RedisDB(AbstractDB):
    def __init__(self):
        super().__init__()
        self.__watchlist = None
        self.connect(config.redis_user, config.redis_pass, config.redis_host, config.redis_port, {})

    def connect(self, username: str, password: str, hostname: str, port: int, options: dict):
        self.__watchlist = redis.StrictRedis(host=config.redis_host,
                                             port=config.redis_port,
                                             db=0,
                                             password=config.redis_pass,
                                             decode_responses=True,
                                             socket_keepalive=True,
                                             retry_on_timeout=True,
                                             retry_on_error=True)
        self.__watchlist.ping()

    def add_thread_to_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist.set(server_id, thread_id)

    def remove_thread_from_watchlist(self, thread_id: str, server_id: str):
        self.__watchlist.delete(server_id)

    def thread_in_watchlist(self, thread_id: str, server_id: str) -> bool:
        res = False
        channel_watchlists = self.__watchlist.get(server_id)
        if thread_id in channel_watchlists:
            res = True
        return res
