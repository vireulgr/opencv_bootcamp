import sys
from PyQt6 import QtWidgets

from ui import MyMainWindow

qApp = QtWidgets.QApplication(sys.argv)

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} <chapter number>')
    exit(0)


chapterNumber = int(sys.argv[1])
if chapterNumber < 1 or chapterNumber > 3:
    print(f'Wrong chapter number: {chapterNumber}; must be between 1 and 3')
    del qApp
    exit(0)

if chapterNumber == 3:
    import basic_image_enhancements
    instance = basic_image_enhancements.classFactory({})
    result = instance.work()

    window = MyMainWindow()

    window.addImageGroup(result[0], 'Addition (brightness)')
    window.addImageGroup(result[1], 'Multiplication (contrast)')
    window.addImageGroup(result[2], 'Threshold')
    window.addImageGroup(result[3], 'Adaptive threshold')
    window.show()

    # maxWidth = 0
    # maxHeight = 0
    # for img in images:
    #     # print(img.shape)
    #     maxWidth = img.shape[1] if img.shape[1] > maxWidth else maxWidth
    #     maxHeight = img.shape[0] if img.shape[0] > maxHeight else maxHeight

    # window.resize(maxWidth + 40, maxHeight)
    window.resize(950, 650)

# elif chapterNumber == 2:
#     import getting_started_with_images
#     exit(getting_started_with_images.run())
#
# elif chapterNumber == 1:
#
#     import basic_image_manipulation
#     exit(basic_image_manipulation.run())
else:
    del qApp
    print(f'not valid chapter name: {chapterNumber}')
    exit(0)

exit(qApp.exec())
