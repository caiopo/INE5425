import re

import strs

REGEX = re.compile(r'([a-z]*)\(([0-9, ]*)\)')


def parse_params(string):
    groups = REGEX.match(string).groups()

    print(groups)

    dist = strs.DISTRIBUTIONS_FUNCS[groups[0]]

    params = groups[1:]

    [int(s.strip()) for s in params.split(',')]


parse_params('')
