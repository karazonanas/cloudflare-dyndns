import logging
import colorlog


class Logger:
    logger = None

    def __init__(self, file_path, logger_name):
        # Create a colorized log formatter
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s %(levelname)-8s %(funcName)-30s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
            secondary_log_colors={},
            style='%'
        )

        fh = logging.FileHandler(f"{file_path}.log")
        sh = logging.StreamHandler()

        fh.setLevel(logging.DEBUG)
        sh.setLevel(logging.INFO)

        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.logger = logging.getLogger(logger_name)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False

    def get_logger(self) -> logging.Logger:
        return self.logger
