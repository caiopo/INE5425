import toga
from colosseum import CSS


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

        buttons = [
            toga.Box(
                children=[
                    toga.Label(key),
                    toga.TextInput(),
                ],
                style=CSS(width=200, margin=20),
            )

            for key in self.distributions.keys()
        ]

        left_box = toga.Box(
            children=[
                toga.Box(children=buttons)
            ],
            style=CSS(width=200, margin=20)
        )

        right_box = toga.Box()

        split = toga.SplitContainer()
        split.content = [left_box, right_box]

        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self
        self.main_window.content = split
        self.main_window.show()


if __name__ == '__main__':
    BaseGui('Simulação', 'br.ufsc.ine.modsim').main_loop()
