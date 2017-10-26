from simulation import distributions

# user strings
TEC1 = 'tec1'
TEC2 = 'tec2'
TS1 = 'ts1'
TS2 = 'ts2'
TEF = 'tef'
TF = 'tf'

TIMES_NAMES = {
    TEC1: 'Tempo entre chegadas 1',
    TEC2: 'Tempo entre chegadas 2',
    TS1: 'Tempo de serviço 1',
    TS2: 'Tempo de serviço 2',
    TEF: 'Tempo entre falhas',
    TF: 'Tempo de falha',
}

DISTRIBUTIONS_NAMES = {
    'constant': 'Constante',
    'exponential': 'Exponencial',
    'normal': 'Normal',
    'triangular': 'Triangular',
    'uniform': 'Uniforme',
}

DISTRIBUTIONS_KEYS = {v: k for k, v in DISTRIBUTIONS_NAMES.items()}

DISTRIBUTIONS_FUNCS = {
    'constant': distributions.constant,
    'exponential': distributions.exponential,
    'normal': distributions.normal,
    'triangular': distributions.triangular,
    'uniform': distributions.uniform,
}
