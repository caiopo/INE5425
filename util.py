import re

import strs

REGEX = re.compile(r'([a-z]*)\(([0-9, ]*)\)')


def parse_params(string):
    groups = REGEX.match(string).groups()

    print(groups)

    dist = strs.DISTRIBUTIONS_FUNCS[groups[0]]

    params = [int(s.strip()) for s in groups[1].split(',')]

    return dist(*params)
