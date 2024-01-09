'''
    this is a module wasya
'''
import sys
import yaml

from pathlib import Path
from PyQt6 import QtWidgets

from ui import MyMainWindow


def getting_started_with_images_():
    import getting_started_with_images
    exit(getting_started_with_images.run())


def basic_image_enhancements_(config):
    import basic_image_enhancements
    instance = basic_image_enhancements.classFactory(config)
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

    # maxWidth = 0
    # maxHeight = 0
    # for img in images:
    #     # print(img.shape)
    #     maxWidth = img.shape[1] if img.shape[1] > maxWidth else maxWidth
    #     maxHeight = img.shape[0] if img.shape[0] > maxHeight else maxHeight

    # window.resize(maxWidth + 40, maxHeight)
    myMainWindow.resize(950, 650)

    return myMainWindow


chaptersDict = {
  3: basic_image_enhancements_
}


def main(argv):

    if len(argv) < 2:
        print(f'usage: {argv[0]} <chapter number>')
        sys.exit(0)

    configPath = Path(argv[0]).parent.parent / 'config.yaml'

    if not configPath.exists():
        raise Exception(f'[E] cannot find config file {configPath}!')

    with open(configPath, 'r') as conf:
        configObject = yaml.load(conf, yaml.Loader)

    if not configObject:
        raise Exception('[E] Cannot load config')

    chapterNumber = int(argv[1])

    if chapterNumber not in chaptersDict:
        print(f'Wrong chapter number: {chapterNumber}; ', end='')
        print(f'must be in ({", ".join(map(str, chaptersDict.keys()))})')
        sys.exit(0)

    assetsDirectory = Path(configObject['common']['assetsRoot']) / str(chapterNumber)

    chapterConfig = configObject['chapters'][chapterNumber - 1]

    chapterConfig.update(assetsDir=assetsDirectory)

    qApp = QtWidgets.QApplication(argv)

    mainWindow = chaptersDict[chapterNumber](chapterConfig)
    mainWindow.show()

    sys.exit(qApp.exec())


if __name__ == '__main__':
    main(sys.argv)
