import logging


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s level=%(levelname)s event=%(message)s',
    )
