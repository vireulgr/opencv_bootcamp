import sys
import yaml
import cv2 as cv
import numpy as np
from pathlib import Path
from PIL import Image

from utils import downloadAndUnzip


class ChapterModule(object):
    configPath = Path(sys.argv[0]).parent.parent / 'config.yaml'
    chapterNumber = 2

    def __init__(self):
        self.configObject = {}

        if not self.configPath.exists():
            raise Exception(f'[E] cannot find config file {self.configPath}!')

        with open(self.configPath, 'r') as conf:
            self.configObject = yaml.load(conf, yaml.Loader)

        if not self.configObject:
            raise Exception('Cannot load config')

        self.configObject = self.configObject['chapters'][self.chapterNumber]

        # print(Path.cwd())
        # print(Path(sys.argv[0]).parent)

        self.assetsDirectory = self.configPath.parent / 'assets' / str(self.chapterNumber + 1)

        self.assetsDirectory.mkdir(parents=True, exist_ok=True)

        assetsZipPath = self.assetsDirectory / self.configObject['resourcesFileName']

        if not assetsZipPath.exists():
            downloadAndUnzip(self.configObject['resourcesUrl'], assetsZipPath)

    def imageAddition(self):
        filePath = self.assetsDirectory / 'New_Zealand_Coast.jpg'
        if not filePath.exists():
            print(f'[E] Path not exists: {str(filePath)}')
            return ()

        imgNewZealandLakeBGR = cv.imread(str(filePath), cv.IMREAD_COLOR)

        addMask = np.ones(imgNewZealandLakeBGR.shape, imgNewZealandLakeBGR.dtype) * 50

        brighterImg = cv.add(imgNewZealandLakeBGR, addMask)
        darkerImg = cv.subtract(imgNewZealandLakeBGR, addMask)

        return (
            Image.fromarray(brighterImg[:, :, ::-1], mode='RGB'),
            Image.fromarray(imgNewZealandLakeBGR[:, :, ::-1], mode='RGB'),
            Image.fromarray(darkerImg[:, :, ::-1], mode='RGB')
        )

    def imageMultiplication(self):
        filePath = self.assetsDirectory / 'New_Zealand_Coast.jpg'
        if not filePath.exists():
            print(f'[E] Path not exists: {str(filePath)}')
            return ()

        imgNewZealandLakeBGR = cv.imread(str(filePath), cv.IMREAD_COLOR)

        mulMask1 = np.ones(imgNewZealandLakeBGR.shape) * 0.8
        mulMask2 = np.ones(imgNewZealandLakeBGR.shape) * 1.2

        imgBlurrier = np.uint8(cv.multiply(np.float64(imgNewZealandLakeBGR), mulMask1))
        imgSharper = np.uint8(np.clip(cv.multiply(np.float64(imgNewZealandLakeBGR), mulMask2), 0, 255))
        # imgSharper = np.uint8(cv.multiply(np.float64(imgNewZealandLakeBGR), mulMask2))
        # print(imgBlurrier.dtype)

        return (
            Image.fromarray(imgBlurrier[:, :, ::-1], mode='RGB'),
            Image.fromarray(imgNewZealandLakeBGR[:, :, ::-1], mode='RGB'),
            Image.fromarray(imgSharper[:, :, ::-1], mode='RGB')
        )

    def thresholdSimple(self):
        filePath = self.assetsDirectory / 'building-windows.jpg'
        if not filePath.exists():
            print(f'[E] Path not exists: {str(filePath)}')
            return ()

        buildingImg = cv.imread(str(filePath), cv.IMREAD_GRAYSCALE)

        _, buildingThreshodedImg = cv.threshold(buildingImg, 100, 255, cv.THRESH_BINARY)

        return (
            Image.fromarray(buildingImg, mode='L'),
            Image.fromarray(buildingThreshodedImg, mode='L')
        )

    def thresholdSheetMusic(self):

        filePath = self.assetsDirectory / 'Piano_Sheet_Music.png'
        if not filePath.exists():
            print(f'[E] Path not exists: {str(filePath)}')
            return ()

        sheetMusicImg = cv.imread(str(filePath), cv.IMREAD_GRAYSCALE)

        _, sheetMusicThresholdedImg = cv.threshold(sheetMusicImg, 130, 255, cv.THRESH_BINARY)

        sheetMusicAdaptiveThresholdedImg = cv.adaptiveThreshold(sheetMusicImg, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 7)

        cv.imwrite(str(self.assetsDirectory / 'Piano_Sheet_Music_thresh.png'), sheetMusicAdaptiveThresholdedImg)

        # print(buildingImg.shape, buildingImg.dtype)
        # print(maskImg.shape, maskImg.dtype)
        return (
            Image.fromarray(sheetMusicImg, mode='L'),
            Image.fromarray(sheetMusicThresholdedImg, mode='L'),
            Image.fromarray(sheetMusicAdaptiveThresholdedImg, mode='L')
        )

    def work(self):
        return (
            self.imageAddition(),
            self.imageMultiplication(),
            self.thresholdSimple(),
            self.thresholdSheetMusic(),
        )


################################################################################
def classFactory(data):

    return ChapterModule()
