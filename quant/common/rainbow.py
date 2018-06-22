import platform
import sys
"""
控制彩色输出
"""
COLORS = dict(
    BLACK = "\u001b[30m",
    RED = "\u001b[31m",
    GREEN = "\u001b[32m",
    YELLOW = "\u001b[33m",
    BLUE = "\u001b[34m",
    MAGENTA = "\u001b[35m",
    CYAN = "\u001b[36m",
    WHITE = "\u001b[37m",

    BBLACK = "\u001b[30;1m",
    BRED = "\u001b[31;1m",
    BGREEN = "\u001b[32;1m",
    BYELLOW = "\u001b[33;1m",
    BBLUE = "\u001b[34;1m",
    BMAGENTA = "\u001b[35;1m",
    BCYAN = "\u001b[36;1m",
    BWHITE = "\u001b[37;1m",
)

RESET = u"\u001b[0m"


class Rainbow:
    """
    在终端上显示有颜色的文字

    当输出被重定向到屏幕以外的文件时不产生颜色控制符；
    在Windows平台的非IPython环境下也不产生颜色控制符。

    Examples
    --------
    ..  code-block::
        python

        from quant.common import Logger, rainbow as rb

        Logger.info(rb.red("This is red"))
        Logger.info(rb.yellow("This is yellow"))
        Logger.info(rb.green("This is green"))
    """
    def __init__(self):
        if self.enable_color():
            self.colors = COLORS
            self.reset = RESET
        else:
            self.colors = {}
            self.reset = ""

    def enable_color(self):
        return self.is_interactive() and (platform.system() != "Windows" or self.is_ipython())
    
    def is_interactive(self):
        return sys.stdout.isatty()

    def is_ipython(self):
        try:
            from IPython import get_ipython, terminal
        except ImportError:
            return False
        return get_ipython()

    def __getattr__(self, name):
        if name.upper() in COLORS.keys():
            return lambda msg: "".join([self.colors.get(name.upper(), ""), msg, self.reset])
        else:
            return super(Rainbow, self).__getattr__(name)


rainbow = Rainbow()
