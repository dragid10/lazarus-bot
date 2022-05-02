from bots import lazarus
from util import logger

# Add loguru logger to all modules
logger = logger.get_logger()


def parse_args():
    """
    Parse command line arguments
    """
    import argparse
    parser = argparse.ArgumentParser(description='Run Lazarus bot')
    parser.add_argument('-d', '--database', type=str, default='memory',
                        help="Database to use to store thread watchlist. Valid options are: 'memory', 'local', and 'redis' (default: memory)")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    lazarus.run(args.database)