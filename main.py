from simulation.distributions import uniform, constant
from simulation.simulation import Simulation, State

if __name__ == '__main__':
    state = State(
        total_time=200,
        tec1=constant(5),
        tec2=constant(5),
        ts1=constant(5),
        ts2=constant(5),
        tef=constant(5),
        tf=constant(5),
    )

    Simulation(state).run_until_complete()
