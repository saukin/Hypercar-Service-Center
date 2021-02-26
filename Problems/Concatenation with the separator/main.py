def concat(arg, *args, sep=' '):
    _output = arg
    for _ in args:
        _output += f'{sep}{_}'
    return _output
