# import sys
# import random
from PySide6 import QtGui
# from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui.MainWindow import Ui_MainWindow


class TEAS(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        # set windows title
        self.setWindowTitle(
            'Transcription and Expressiveness Annotation System 2.0')
        # set application icon
        icon_path = './assets/pic/TEAS_icon.png'
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)

        self.MyPushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = QApplication([])
    window = TEAS()
    window.show()
    app.exec()
