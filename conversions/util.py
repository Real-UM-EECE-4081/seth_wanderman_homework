def conv(value, fromX, toY):
    td = {
           'C': lambda val: val + 273.15,
           'F': lambda val: (val + 459.67)*5/9,
            }
    fd = {
             'C': lambda val: val - 273.15,
             'F': lambda val: val*9/5 - 459.67,
            }

    try:
        temp = td[fromX](value)
    except KeyError:
        raise ValueError('Unrecognized temperature unit: {}'.format(fromX))

    if temp < 0:
        raise ValueError('Invalid temperature: {} {} is less than 0'.format(value, fromX))

    if fromX == toY:
        return value

    try:
        return fd[toY](temp)
    except KeyError:
        raise ValueError('Unrecognized temperature unit: {}'.format(toY))