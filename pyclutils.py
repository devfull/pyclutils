import subprocess
import functools
import itertools


def hint_last(iterable):
    try:
        iterable = iter(iterable)
        a = next(iterable)
        for b in iterable:
            yield (a, False)
            a = b
        yield (a, True)
    except StopIteration:
        return


def instruction(option=None):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(self, *args, **kwargs):
            command = [option or function.__name__]
            for key, value in kwargs.items():
                command.append('--' + key)
                if value is True:
                    continue
                command.append(str(value))
            command.extend([str(x) for x in args])

            self.instructions.append(command)
            self.parsers.append(function(self, *args, **kwargs))

            return self
        return wrapper
    return decorator


class ShellCommand():
    def __init__(self, executable):
        self.executable = executable
        self.clean()

    def clean(self):
        self.instructions = []
        self.modifiers = []
        self.parsers = []

        return self

    def run(self, stdin=None, stdout=True, stderr=True):
        self.outputs = []

        proc = subprocess.Popen(
                [self.executable] + list(itertools.chain(*self.instructions)),
                stdin=subprocess.PIPE  if stdin  else None,
                stdout=subprocess.PIPE if stdout else None,
                stderr=subprocess.PIPE if stderr else None,
                universal_newlines=True
        )

        proc.stdout, proc.stderr = proc.communicate(stdin)

        self.stdout = proc.stdout
        self.stderr = proc.stderr
        self.status = proc.returncode

        if proc.returncode or not stdout:
            return self.clean()

        it = iter(self.stdout.rstrip().split('\n'))
        ig = iter(self.stdout.rstrip().split('\n'))
        xs = zip(self.instructions, self.parsers)

        for ((command, *_), parser), last in hint_last(xs):
            if (parser and not (command in self.modifiers and not last)):
                self.outputs.append(parser(it))

        return self.clean()
