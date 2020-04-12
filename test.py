

import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QDialog, QApplication
import time


class BigThingThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, rest, parent=None):
        super().__init__(parent)
        self._rest = rest

    def run(self):
        print('do something big')
        time.sleep(self._rest)
        self.finished_signal.emit('done')


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton(self)
        self.button.setText('干大事')
        self.button.clicked.connect(self._click_do_something)

    @staticmethod
    def _show_message(message):
        print('{}'.format(message))

    def _click_do_something(self):
        self.big_thread = BigThingThread(1)
        self.big_thread.finished_signal.connect(self._show_message)
        self.big_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())