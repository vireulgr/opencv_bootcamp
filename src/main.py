'''
    this is a module wasya
'''
import sys
import yaml

from pathlib import Path
from PyQt6 import QtWidgets

from ui import MyMainWindow

qApp = QtWidgets.QApplication(sys.argv)

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} <chapter number>')
    sys.exit(0)


configPath = Path(sys.argv[0]).parent.parent / 'config.yaml'

if not configPath.exists():
    raise Exception(f'[E] cannot find config file {configPath}!')

with open(configPath, 'r') as conf:
    configObject = yaml.load(conf, yaml.Loader)

if not configObject:
    raise Exception('Cannot load config')


chapterNumber = int(sys.argv[1])

assetsDirectory = Path(configObject['common']['assetsRoot']) / str(chapterNumber)

chapterConfig = configObject['chapters'][chapterNumber - 1]

chapterConfig.update(assetsDir=assetsDirectory)

if chapterNumber < 1 or chapterNumber > 3:
    print(f'Wrong chapter number: {chapterNumber}; must be between 1 and 3')
    del qApp
    sys.exit(0)

if chapterNumber == 3:
    import basic_image_enhancements
    instance = basic_image_enhancements.classFactory(chapterConfig)
    result = instance.work()

    myMainWindow = MyMainWindow()

    myMainWindow.addImageGroup(result[0], 'Addition (brightness)')
    myMainWindow.addImageGroup(result[1], 'Multiplication (contrast)')
    myMainWindow.addImageGroup(result[2], 'Threshold')
    myMainWindow.addImageGroup(result[3], 'Adaptive threshold')
    myMainWindow.addImageGroup(result[4], 'Sample images for bitwise operations')
    myMainWindow.addImageGroup(result[5], 'Bitwise and, bitwise or, bitwise xor')
    myMainWindow.addImageGroup(result[6], 'Images for task')
    myMainWindow.addImageGroup(result[7], 'Task process 1')
    myMainWindow.show()

    # maxWidth = 0
    # maxHeight = 0
    # for img in images:
    #     # print(img.shape)
    #     maxWidth = img.shape[1] if img.shape[1] > maxWidth else maxWidth
    #     maxHeight = img.shape[0] if img.shape[0] > maxHeight else maxHeight

    # window.resize(maxWidth + 40, maxHeight)
    myMainWindow.resize(950, 650)

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
    sys.exit(0)

sys.exit(qApp.exec())
