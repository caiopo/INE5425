from distributions import uniform
from simulation import Simulation, State

if __name__ == '__main__':
    state = State(
        total_time=200,
        tec1=uniform(5, 10),
        tec2=uniform(5, 10),
        ts1=uniform(5, 10),
        ts2=uniform(5, 10),
        tef=uniform(5, 10),
        tf=uniform(5, 10),
    )

    Simulation(state).run_until_complete()
