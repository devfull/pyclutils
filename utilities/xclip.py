from ..pyclutils import ShellCommand
from ..pyclutils import instruction

class Xclip(ShellCommand):
    def __init__(self):
        return super().__init__('xclip')

    def run(self, stdin=False, stdout=True, stderr=None):
        return super().run(stdin, stdout, stderr)

    @instruction('-f')
    def filter(self, *args, **kwargs):
        pass

    @instruction('-o')
    def out(self, *args, **kwargs):
        pass

    @instruction('-selection')
    def selection(self, *args, **kwargs):
        pass

    def copy(self, stdin):
        return self.filter().run(stdin)

    def paste(self):
        return self.out().run()
