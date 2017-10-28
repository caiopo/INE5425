import sys

from PyQt5 import QtWidgets

import strs
from mainwindow import Ui_MainWindow
from simulation import reports, State, Simulation
from util import parse_params, try_int


class Main:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

        self.simulation = None

        self.finish(None)

        # debug
        self.ui.tec1_text.setText('1')
        self.ui.tec2_text.setText('1')
        self.ui.ts1_text.setText('1')
        self.ui.ts2_text.setText('1')
        self.ui.tef_text.setText('1')
        self.ui.tf_text.setText('1')

        self.handle_slider()
        self.ui.nsteps.valueChanged.connect(self.handle_slider)
        self.ui.start.clicked.connect(self.button_start)
        self.ui.step.clicked.connect(self.button_step)
        self.ui.complete.clicked.connect(self.button_complete)
        self.ui.stop.clicked.connect(self.button_cancel)

        sys.exit(self.app.exec_())

    def update_labels(self, state):
        if state is None:
            self.ui.mean_entity_in_queue_1.setText("--")
            self.ui.mean_entity_in_queue_2.setText("--")
            self.ui.occupation_rate_1.setText("--")
            self.ui.occupation_rate_2.setText("--")
            self.ui.mean_time_in_queue.setText("--")
            self.ui.mean_time_in_system.setText("--")
            self.ui.entities_entered.setText("--")
            self.ui.entities_left.setText("--")
            self.ui.entities_inside.setText("--")
            self.ui.entities_blocked.setText("--")
            self.ui.fail_rate_1.setText("--")
            self.ui.fail_rate_2.setText("--")
            self.ui.fix_count_1.setText("--")
            self.ui.fix_count_2.setText("--")

            self.ui.progress_bar.setValue(0)
            set_text(self.ui.time, 0)

        else:
            stats = self.simulation.state.statistics
            svrs = self.simulation.state.servers
            sv1, sv2 = svrs

            set_text(self.ui.mean_entity_in_queue_1, None)
            set_text(self.ui.mean_entity_in_queue_2, None)
            set_text(self.ui.occupation_rate_1, reports.occupation_rate(sv1))
            set_text(self.ui.occupation_rate_2, reports.occupation_rate(sv2))
            set_text(self.ui.mean_time_in_queue, reports.mean_time_in_queue(svrs))
            set_text(self.ui.mean_time_in_system, reports.mean_time_in_system(svrs))
            set_text(self.ui.entities_entered, stats.entities_entered)
            set_text(self.ui.entities_left, stats.entities_left)
            set_text(self.ui.entities_inside, stats.entities_entered - stats.entities_left)
            set_text(self.ui.entities_blocked, stats.entities_blocked)
            set_text(self.ui.fail_rate_1, reports.fail_rate(sv1))
            set_text(self.ui.fail_rate_2, reports.fail_rate(sv2))
            set_text(self.ui.fix_count_1, len(sv1.fails))
            set_text(self.ui.fix_count_2, len(sv2.fails))

            if state.finished:
                self.ui.progress_bar.setValue(100)
            else:
                if state.total_time is None or state.total_time == 0:
                    self.ui.progress_bar.setValue(50)
                else:
                    self.ui.progress_bar.setValue(int(100 * state.current_time / state.total_time))

            set_text(self.ui.time, int(state.current_time))

        self.ui.error.setText("")

    def start(self, state):
        widgets_to_enable = (
            self.ui.complete, self.ui.step,
        )

        widgets_to_disable = (
            self.ui.tec1_cb, self.ui.tec1_text,
            self.ui.tec2_cb, self.ui.tec2_text,
            self.ui.ts1_cb, self.ui.ts1_text,
            self.ui.ts2_cb, self.ui.ts2_text,
            self.ui.tef_cb, self.ui.tef_text,
            self.ui.tf_cb, self.ui.tf_text,
            self.ui.entity_limit, self.ui.total_time,
            self.ui.start,
        )

        for widget in widgets_to_enable:
            widget.setEnabled(True)

        for widget in widgets_to_disable:
            widget.setEnabled(False)

        if state.total_time is None:
            self.ui.complete.setEnabled(False)

    def finish(self, state):
        widgets_to_enable = (
            self.ui.tec1_cb, self.ui.tec1_text,
            self.ui.tec2_cb, self.ui.tec2_text,
            self.ui.ts1_cb, self.ui.ts1_text,
            self.ui.ts2_cb, self.ui.ts2_text,
            self.ui.tef_cb, self.ui.tef_text,
            self.ui.tf_cb, self.ui.tf_text,
            self.ui.entity_limit, self.ui.total_time,
            self.ui.start, self.ui.complete
        )

        widgets_to_disable = (
            self.ui.complete, self.ui.step,
        )

        for widget in widgets_to_enable:
            widget.setEnabled(True)

        for widget in widgets_to_disable:
            widget.setEnabled(False)

        self.update_labels(state)

    def handle_slider(self):
        steps = self.ui.nsteps.value()
        self.ui.step.setText('Avançar {} unidades de tempo'.format(str(steps).zfill(2)))

    def button_start(self):
        params = self.get_params()

        if params is None:
            return

        state = State(**params)

        self.simulation = Simulation(state)

        self.update_labels(self.simulation.state)

        self.start(state)

    def button_step(self):
        steps = self.ui.nsteps.value()

        if steps < 1:
            return

        state = None

        for _ in range(self.ui.nsteps.value()):
            state = self.simulation.step()

        if state.finished:
            self.finish(state)
        else:
            self.update_labels(state)

    def button_complete(self):
        state = self.simulation.step()

        while not state.finished:
            for _ in range(100):
                state = self.simulation.step()
            self.update_labels(state)

        self.finish(state)

    def button_cancel(self):
        self.finish(None)
        self.simulation = None

    def get_params(self):
        dist_widgets = {
            'tec1': (self.ui.tec1_cb, self.ui.tec1_text),
            'tec2': (self.ui.tec2_cb, self.ui.tec2_text),
            'ts1': (self.ui.ts1_cb, self.ui.ts1_text),
            'ts2': (self.ui.ts2_cb, self.ui.ts2_text),
            'tef': (self.ui.tef_cb, self.ui.tef_text),
            'tf': (self.ui.tf_cb, self.ui.tf_text),
        }

        params = {}

        try:
            for (key, (cb, text)) in dist_widgets.items():
                dist_name = strs.DISTRIBUTIONS_BY_INDEX[cb.currentIndex()]

                params[key] = parse_params(dist_name, text.text())

            params['entity_limit'] = try_int(self.ui.entity_limit.text())
            params['total_time'] = try_int(self.ui.total_time.text())

        except Exception as e:
            print(e)
            self.ui.error.setText("Erro no preenchimento de um campo")
        else:
            return params


def set_text(widget, value):
    if value is None:
        widget.setText('--')
    elif isinstance(value, float):
        widget.setText('{:f}'.format(value))
    else:
        widget.setText(str(value))


if __name__ == '__main__':
    Main()
