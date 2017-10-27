import toga
from colosseum import CSS

import strs


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

        left_box = toga.Box(
            children=(children +
                      [toga.Button(
                          'Confirmar',
                          on_press=self.save_params,
                          style=CSS(width=200, margin=20))]),
            style=CSS(width=200, margin=20),
        )

        right_box = toga.Box()

        split = toga.SplitContainer()
        split.content = [left_box, right_box]

        self.main_window = toga.Window(self.name)
        self.main_window.app = self
        self.main_window.content = split
        self.main_window.show()

    def save_params(self, button):
        params = {k: ti.value for k, ti in self.inputs.items()}

        

if __name__ == '__main__':
    BaseGui('Simulação', 'br.ufsc.ine.modsim').main_loop()
