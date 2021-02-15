import functools

from ..pyclutils import ShellCommand
from ..pyclutils import instruction
from ..parsers import findall_int
from ..parsers import consume

class Xdotool(ShellCommand):
    def __init__(self):
        return super().__init__('xdotool')

    def windowstack_modifier(function):
        @functools.wraps(function)
        def wrapper(self, *args, **kwargs):
            self.modifiers.append(function.__name__)

            return function(self, *args, **kwargs)
        return wrapper

# KEYBOARD COMMANDS

    @instruction()
    def key(self, *args, **kwargs):
        pass

    @instruction()
    def keydown(self, *args, **kwargs):
        pass

    @instruction()
    def keyup(self, *args, **kwargs):
        pass

    @instruction()
    def type(self, *args, **kwargs):
        pass

# MOUSE COMMANDS

    @instruction()
    def mousemove(self, *args, **kwargs):
        pass

    @instruction()
    def mousemove_relative(self, *args, **kwargs):
        pass

    @instruction()
    def click(self, *args, **kwargs):
        pass

    @instruction()
    def mousedown(self, *args, **kwargs):
        pass

    @instruction()
    def mouseup(self, *args, **kwargs):
        pass

    @instruction()
    def getmouselocation(self, *args, **kwargs):
        def parser(iterator):
            keys = ['x', 'y', 'screen', 'window']

            if ('shell' in kwargs):
                iterator = zip(*[iterator] * 4)

            return dict(zip(keys, findall_int(next(iterator))))
        return parser

    @instruction()
    def behave_screen_edge(self, *args, **kwargs):
        pass

# WINDOW COMMANDS

    @instruction()
    @windowstack_modifier
    def search(self, *args, **kwargs):
        def parser(iterator):
            return consume(iterator, all=True)
        return parser

    @instruction()
    @windowstack_modifier
    def selectwindow(self, *args, **kwargs):
        return consume

    @instruction()
    def behave(self, *args, **kwargs):
        pass

    @instruction()
    def getwindowpid(self, *args, **kwargs):
        def parser(iterator):
            return consume(iterator, all='%@' in args)
        return parser

    @instruction()
    def getwindowname(self, *args, **kwargs):
        def parser(iterator):
            return consume(iterator, str, all='%@' in args)
        return parser

    @instruction()
    def getwindowgeometry(self, *args, **kwargs):
        def parser(iterator):
            if ('shell' in kwargs):
                iterator = zip(*[iterator] * 6)
                keys = ['window', 'x', 'y', 'width', 'height', 'screen']
            else:
                keys = ['window', 'x', 'y', 'screen', 'width', 'height']
                iterator = zip(*[iterator] * 3)

            iterator = (zip(keys, findall_int(xs)) for xs in iterator)

            return consume(iterator, dict, all='%@' in args)
        return parser

    @instruction()
    @windowstack_modifier
    def getwindowfocus(self, *args, **kwargs):
        return consume

    @instruction()
    def windowsize(self, *args, **kwargs):
        pass

    @instruction()
    def windowfocus(self, *args, **kwargs):
        pass

    @instruction()
    def windowmap(self, *args, **kwargs):
        pass

    @instruction()
    def windowminimize(self, *args, **kwargs):
        pass

    @instruction()
    def windowraise(self, *args, **kwargs):
        pass

    @instruction()
    def windowreparent(self, *args, **kwargs):
        pass

    @instruction()
    def windowclose(self, *args, **kwargs):
        pass

    @instruction()
    def windowkill(self, *args, **kwargs):
        pass

    @instruction()
    def windowunmap(self, *args, **kwargs):
        pass

    @instruction()
    def set_window(self, *args, **kwargs):
        pass

# DESKTOP AND WINDOW COMMANDS

    @instruction()
    def windowactivate(self, *args, **kwargs):
        pass

    @instruction()
    @windowstack_modifier
    def getactivewindow(self, *args, **kwargs):
        return consume

    @instruction()
    def set_num_desktops(self, *args, **kwargs):
        pass

    @instruction()
    def get_num_desktops(self, *args, **kwargs):
        return consume

    @instruction()
    def get_desktop_viewport(self, *args, **kwargs):
        def parser(iterator):
            if ('shell' in kwargs):
                iterator = zip(*[iterator] * 2)

            return dict(zip(['x', 'y'], findall_int(next(iterator))))
        return parser

    @instruction()
    def set_desktop_viewport(self, *args, **kwargs):
        pass

    @instruction()
    def set_desktop(self, *args, **kwargs):
        pass

    @instruction()
    def get_desktop(self, *args, **kwargs):
        return consume

    @instruction()
    def set_desktop_for_window(self, *args, **kwargs):
        pass

    @instruction()
    def get_desktop_for_window(self, *args, **kwargs):
        return consume

# MISCELLANEOUS COMMANDS

    @instruction()
    def exec(self, *args, **kwargs):
        pass

    @instruction()
    def sleep(self, *args, **kwargs):
        pass
