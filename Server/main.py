import sys
import ps
import threading
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from main_ui import Ui_Server

class Window(QMainWindow, Ui_Server):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.check = False
        self.pushButton.clicked.connect(self.start)
    def start(self):
        if (self.check == False):
            self.check = True
            self.pushButton.setText("Started")
            self.pushButton.setEnabled(False)
            d = threading.Thread(name='daemon', target=ps.main)
            d.start()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
