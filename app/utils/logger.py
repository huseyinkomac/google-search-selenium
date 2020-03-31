import logging


class Logger:
    def __init__(self, fn, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s: %(pathname)s %(levelname)s %(funcName)s (%(lineno)d) -- %(message)s'
        )

        fh = logging.FileHandler(f"../logs/{fn}.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger

    def disable_logger(self):
        self.logger.disabled = True

    def enable_logger(self):
        self.logger.disabled = False
