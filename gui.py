import toga
from colosseum import CSS

import strs
from simulation import simulation
from util import parse_params


# noinspection PyAttributeOutsideInit
class BaseGui(toga.App):
    def startup(self):
        self.distributions = {
            'tec1': None,
            'tec2': None,
            'ts1': None,
            'ts2': None,
            'tef': None,
            'tf': None,
        }

        self.inputs = {
            key: toga.TextInput()
            for key in self.distributions.keys()
        }

        self.input_total_time = toga.TextInput()
        self.input_entity_limit = toga.TextInput()

        children = [
            toga.Box(
                children=[
                    toga.Label(strs.TIMES_NAMES[key]),
                    self.inputs[key],
                ],
                style=CSS(width=200, margin_bottom=10),
            )

            for key in self.distributions.keys()
        ]

        children.append(
            toga.Box(
                children=[
                    toga.Label('Tempo máximo de simulação'),
                    self.input_total_time,
                ],
                style=CSS(width=200, margin_bottom=10),
            ))

        children.append(
            toga.Box(
                children=[
                    toga.Label('Máximo de entidades'),
                    self.input_entity_limit,
                ],
                style=CSS(width=200, margin_bottom=10),
            ))

        self.confirm_button = toga.Button(
            'Confirmar',
            on_press=self.confirm,
            style=CSS(width=200, margin=20),
        )

        left_box = toga.Box(
            children=(children + [self.confirm_button]),
            style=CSS(width=200, margin=20),
        )

        right_box = toga.Box()

        split = toga.SplitContainer()
        split.content = [left_box, right_box]

        self.main_window = toga.Window(self.name, position=(600, 100), size=(640, 680), resizeable=False)
        self.main_window.app = self
        self.main_window.content = split
        self.main_window.show()

    def confirm(self, button):
        try:
            self.distributions = {k: parse_params(ti.value) for k, ti in self.inputs.items()}

            total_time = int(self.input_total_time.value)
            entity_limit = int(self.input_entity_limit.value)
        except Exception as e:
            print(e)
            return

        self.state = simulation.State(total_time=total_time, entity_limit=entity_limit, **self.distributions)

        # def create_commands(self):
        #     cmd1 = toga.Command(
        #         lambda: print('oi'),
        #         label='Iniciar simulação',
        #         tooltip='Inicia a simulação',
        #         # icon=toga.Icon.TIBERIUS_ICON,
        #     )
        #
        #     return [cmd1]


        if __name__ == '__main__':
            BaseGui('Simulação', 'br.ufsc.ine.modsim').main_loop()
