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
    def __init__(self):
        if self.is_interactive():
            self.colors = COLORS
            self.reset = RESET
        else:
            self.colors = {}
            self.reset = ""

    @staticmethod
    def is_interactive():
        try:
            from IPython import get_ipython, terminal
        except ImportError:
            # 没有安装IPython
            return sys.stdout.isatty() and platform.system() != "Windows"
        this = get_ipython()
        if not this:
            # 普通Python环境，不是IPython
            return sys.stdout.isatty() and platform.system() != "Windows"
        elif isinstance(this, terminal.interactiveshell.TerminalInteractiveShell):
            # IPython的命令环境
            return sys.stdout.isatty()
        else:
            # Notebook环境
            return True

    def __getattr__(self, name):
        if name.upper() in COLORS.keys():
            return lambda msg: "".join([self.colors.get(name.upper(), ""), msg, self.reset])
        else:
            return super(Rainbow, self).__getattr__(name)


rainbow = Rainbow()
