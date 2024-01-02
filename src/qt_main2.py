from PyQt5.QtWidgets import  *
from PyQt5.QtCore import  *
from PyQt5.QtGui import  *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Hello PyQt5!!!')
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        label = QLabel('this is awesome!')

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        self. setWindowTitle("My awesome app!")

    def my_custom_fn(self, arg = 'hello'):
        print(arg)


    def onWindowTitleChange(self, title):
        print(title)


    # has the same name as in parent class
    def contextMenuEvent(self, event):
        super(MainWindow, self).contextMenuEvent(event)


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()

