def mal_read(arg: str) -> str:
    return arg


def mal_eval(arg: str) -> str:
    return arg


def mal_print(arg: str) -> str:
    return arg


def rep(arg: str) -> str:
    return mal_print(mal_eval(mal_read(arg)))


if __name__ == '__main__':
    line = input('user> ')
    while line != '':
        rep(line)
        line = input('user> ')