from simulation.distributions import uniform, constant
from simulation.simulation import Simulation, State

if __name__ == '__main__':
    state = State(
        total_time=200,
        tec1=constant(5),
        tec2=constant(6),
        ts1=constant(7),
        ts2=constant(8),
        tef=constant(9),
        tf=constant(10),
    )

    simulation = Simulation(state)

    while not simulation.state.finished:
        simulation.step()
        print(state.statistics)
