from datetime import datetime
from richenum import OrderedRichEnum, OrderedRichEnumValue
from ..common.rainbow import rainbow
from ..common.settings import CONFIG


class LoggingLevel(OrderedRichEnum):
    DEBUG = OrderedRichEnumValue(index=1, canonical_name='DEBUG', display_name='DEBUG')
    INFO = OrderedRichEnumValue(index=2, canonical_name='INFO', display_name='INFO')
    WARNING = OrderedRichEnumValue(index=3, canonical_name='WARNING', display_name='WARNING')
    ERROR = OrderedRichEnumValue(index=4, canonical_name='ERROR', display_name='ERROR')
    FATAL = OrderedRichEnumValue(index=5, canonical_name='FATAL', display_name='FATAL')


colors = {
    "DEBUG": "cyan",
    "INFO": "blue",
    "WARNING": "magenta",
    "ERROR": "bred",
    "FATAL": "red",
}


class Logger:
    @staticmethod
    def log(*msgs, level=LoggingLevel.INFO):
        if level >= getattr(LoggingLevel, CONFIG.LOG_LEVEL.upper()):
            print("[{level}] {dt}".format(
                level=getattr(rainbow, colors[level.display_name])(level.display_name),
                dt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ), *msgs)

    @classmethod
    def debug(cls, *msgs):
        return cls.log(*msgs, level=LoggingLevel.DEBUG)

    @classmethod
    def info(cls, *msgs):
        return cls.log(*msgs, level=LoggingLevel.INFO)

    @classmethod
    def warn(cls, *msgs):
        return cls.log(*msgs, level=LoggingLevel.WARNING)

    @classmethod
    def error(cls, *msgs):
        return cls.log(*msgs, level=LoggingLevel.ERROR)

    @classmethod
    def fatal(cls, *msgs):
        return cls.log(*msgs, level=LoggingLevel.FATAL)
    