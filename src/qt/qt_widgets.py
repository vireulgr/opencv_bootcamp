from PyQt6 import QtWidgets

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('App')

        layout = QtWidgets.QVBoxLayout()

        widgets = [ QtWidgets.QCheckBox,
                   QtWidgets.QComboBox,
                   QtWidgets.QDateEdit,
                   QtWidgets.QDateTimeEdit,
                   QtWidgets.QDial,
                   QtWidgets.QDoubleSpinBox,
                   QtWidgets.QLCDNumber,
                   QtWidgets.QLabel,
                   QtWidgets.QLineEdit,
                   QtWidgets.QProgressBar,
                   QtWidgets.QPushButton,
                   QtWidgets.QRadioButton,
                   QtWidgets.QSlider,
                   QtWidgets.QSpinBox,
                   QtWidgets.QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()

