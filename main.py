from bots import lazarus
from util import logger

# Add loguru logger to all modules
logger = logger.get_logger()

if __name__ == '__main__':
    lazarus.run()
