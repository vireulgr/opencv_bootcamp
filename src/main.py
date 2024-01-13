'''
    this is a main module
'''
import sys
import yaml

from pathlib import Path
from PyQt6 import QtWidgets

from ui import MyMainWindow


def loadConfigForChapter(chapterNumber):
    configPath = Path(str(chapterNumber)).parent.parent / 'config.yaml'

    if not configPath.exists():
        raise Exception(f'[E] cannot find config file {configPath}!')

    with open(configPath, 'r') as conf:
        configObject = yaml.load(conf, yaml.Loader)

    assetsDirectory = Path(configObject['common']['assetsRoot']) / str(chapterNumber)

    chapterConfig = configObject['chapters'][chapterNumber - 1]

    chapterConfig.update(assetsDir=assetsDirectory)

    return chapterConfig


def getting_started_with_images_():
    import getting_started_with_images
    exit(getting_started_with_images.run())


def basic_image_enhancements_(config):
    import basic_image_enhancements
    instance = basic_image_enhancements.classFactory(config)
    result = instance.work()

    qApp = QtWidgets.QApplication([])

    myMainWindow = MyMainWindow()

    myMainWindow.addImageGroup(result[0], 'Addition (brightness)')
    myMainWindow.addImageGroup(result[1], 'Multiplication (contrast)')
    myMainWindow.addImageGroup(result[2], 'Threshold')
    myMainWindow.addImageGroup(result[3], 'Adaptive threshold')
    myMainWindow.addImageGroup(result[4], 'Sample images for bitwise operations')
    myMainWindow.addImageGroup(result[5], 'Bitwise and, bitwise or, bitwise xor')
    myMainWindow.addImageGroup(result[6], 'Images for task')
    myMainWindow.addImageGroup(result[7], 'Image overlay')

    myMainWindow.setWindowTitle('Image enhancements')
    myMainWindow.resize(950, 650)
    myMainWindow.show()

    sys.exit(qApp.exec())


def video_intro_(config):
    import video_intro
    instance = video_intro.classFactory(config)
    try:
        instance.init()
        instance.show()
    except Exception as e:
        print('Exception!', str(e))
    finally:
        instance.cleanup()

def video_writing_(config):
    import video_writing
    instance = video_writing.classFactory(config)
    try:
        instance.init()
        instance.writeToDisk()
        # instance.show()
    except Exception as e:
        print('Exception!', str(e))
    finally:
        instance.cleanup()


chaptersDict = {
    2: getting_started_with_images_,
    3: basic_image_enhancements_,
    4: video_intro_,
    5: video_writing_,
}


def main(argv):

    if len(argv) < 2:
        print(f'usage: {argv[0]} <chapter number>')
        sys.exit(0)

    chapterNumber = int(argv[1])

    if chapterNumber not in chaptersDict:
        print(f'Wrong chapter number: {chapterNumber}; ', end='')
        print(f'must be in ({", ".join(map(str, chaptersDict.keys()))})')
        sys.exit(0)

    chapterConfig = loadConfigForChapter(chapterNumber)

    chaptersDict[chapterNumber](chapterConfig)


if __name__ == '__main__':
    main(sys.argv)

