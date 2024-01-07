from PyQt6 import QtWidgets, QtGui
from PIL import ImageQt


# https://stackoverflow.com/q/63528165
class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, pilImages=[], *args, **kwargs):
        super().__init__(*args, **kwargs)

        # scroll area 1: https://stackoverflow.com/q/28818323
        # scroll area 2: https://stackoverflow.com/q/3117911
        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        # scrollArea.setGeometry(5, 5, 840, 790)

        mainWidget = QtWidgets.QWidget()

        self.verticalLayout = QtWidgets.QVBoxLayout()

        mainWidget.setLayout(self.verticalLayout)

        scrollArea.setWidget(mainWidget)

        self.pixMaps = []
        self.qLabels = []
        self.qtImages = []

        self.addImageGroup(pilImages)

        self.setCentralWidget(scrollArea)

    # def printValues(self):
    #     for pix in self.pixMaps:
    #         aQImage = pix.toImage()

    #         x = 2
    #         y = 2
    #         rgbValue = aQImage.pixel(x, y)
    #         print(f'{x},{y}: {QtGui.qRed(rgbValue)}, {QtGui.qGreen(rgbValue)}, {QtGui.qBlue(rgbValue)}')

    def addImageGroup(self, imageGroup, title=''):
        if len(imageGroup) < 1:
            return

        horizontalLayout = QtWidgets.QHBoxLayout()

        for idx, pilImage in enumerate(imageGroup, start=(len(self.qtImages))):

            self.qtImages.append(ImageQt.ImageQt(pilImage))
            qPixMap = QtGui.QPixmap.fromImage(self.qtImages[idx])
            self.pixMaps.append(qPixMap.scaledToWidth(300))

            self.qLabels.append(QtWidgets.QLabel())

            self.qLabels[idx].setPixmap(self.pixMaps[idx])

            # QLabel box shape
            # https://stackoverflow.com/q/44555064
            # https://doc.qt.io/qt-6/qframe.html#Shape-enum
            self.qLabels[idx].setFrameShape(QtWidgets.QFrame.Shape.Box)
            horizontalLayout.addWidget(self.qLabels[idx])

        if len(title) > 0:
            self.verticalLayout.addWidget(QtWidgets.QLabel(title))

        self.verticalLayout.addLayout(horizontalLayout)
