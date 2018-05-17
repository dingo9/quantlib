from datetime import datetime
from richenum import OrderedRichEnum, OrderedRichEnumValue
from ..common.settings import CONFIG


class LoggingLevel(OrderedRichEnum):
    DEBUG = OrderedRichEnumValue(index=1, canonical_name='DEBUG', display_name='DEBUG')
    INFO = OrderedRichEnumValue(index=2, canonical_name='INFO', display_name='INFO')
    WARNING = OrderedRichEnumValue(index=3, canonical_name='WARNING', display_name='WARNING')
    ERROR = OrderedRichEnumValue(index=4, canonical_name='ERROR', display_name='ERROR')
    FATAL = OrderedRichEnumValue(index=5, canonical_name='FATAL', display_name='FATAL')


colors = {
    "DEBUG": "\u001b[36m",    # CYAN
    "INFO": "\u001b[34m",     # BLUE
    "WARNING": "\u001b[35m",  # MEGENTA
    "ERROR": "\u001b[31;1m",  # BRED
    "FATAL": "\u001b[31m"     # RED
}


class Logger:
    @staticmethod
    def log(msg, level=LoggingLevel.INFO):
        if level >= getattr(LoggingLevel, CONFIG.LOG_LEVEL.upper()):
            print("[{color}{level}{reset}] {dt} {msg}".format(
                color=colors[level.display_name],
                level=level.display_name,
                reset="\u001b[0m",
                dt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                msg=msg,
            ))

    @classmethod
    def debug(cls, msg):
        return cls.log(msg, level=LoggingLevel.DEBUG)

    @classmethod
    def info(cls, msg):
        return cls.log(msg, level=LoggingLevel.INFO)

    @classmethod
    def warn(cls, msg):
        return cls.log(msg, level=LoggingLevel.WARNING)

    @classmethod
    def error(cls, msg):
        return cls.log(msg, level=LoggingLevel.ERROR)

    @classmethod
    def fatal(cls, msg):
        return cls.log(msg, level=LoggingLevel.FATAL)
    