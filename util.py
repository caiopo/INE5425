import re

import strs

REGEX = re.compile(r'([0-9.]*)')

ALLOWED_CHARS = set('0123456789. ')


def parse_params(dist_name, text):
    if not set(text).issubset(ALLOWED_CHARS):
        raise ValueError()

    groups = REGEX.match(text).groups()

    print(groups)

    dist = strs.DISTRIBUTIONS_FUNCS[dist_name]

    params = [float(s.strip()) for s in groups]

    return dist(*params)


def try_int(string):
    if len(string) != 0:
        return int(string)

    return None
