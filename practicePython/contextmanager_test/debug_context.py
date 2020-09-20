import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.INFO)

@contextmanager
def debug_context():
    level = logger.level
    try:
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        logger.setLevel(level)

def main():
    logger.info("before: info log")
    logger.debug("before: debug log")

    with debug_context():
        logger.info("inside: info log")
        logger.debug("inside: debug log")

    logger.info("after: info log")
    logger.debug("after: debug log")


if __name__ == '__main__':
    main()