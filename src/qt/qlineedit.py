from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MySampleWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MySampleWindow, self).__init__(*args, **kwargs)
        lineEdit = QLineEdit()
        lineEdit.setMaxLength(10)
        lineEdit.setPlaceholderText('enter your text')

        self.setCentralWidget(lineEdit)


app = QApplication(sys.argv);


window = MySampleWindow()

window.show()


app.exec_()
