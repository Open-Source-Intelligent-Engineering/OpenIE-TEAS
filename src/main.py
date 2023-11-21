import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class TEAS(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # set windows title
        self.setWindowTitle(
            'Transcription and Expressiveness Annotation System 2.0')
        # set application icon
        icon_path = './assets/pic/TEAS_icon.png'
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)
        # Fix window size
        self.setFixedSize(1120, 720)
        # add other UI initialization here
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = TEAS()
    sys.exit(app.exec())
