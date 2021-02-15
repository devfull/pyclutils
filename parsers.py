import re


def findall_int(*args):
    return [int(n) for n in re.findall('\d+', str(args))]


def consume(iterable, function=int, all=False):
    return (list if(all) else next)(map(function, iterable))
