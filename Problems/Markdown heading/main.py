def heading(text, level=0):
    _hash = '#'
    output = ''
    if level <= 1:
        output = f'{_hash} {text}'
    elif level > 6:
        output = f'{_hash * 6} {text}'
    else:
        output = f'{_hash * level} {text}'

    return output
