import cv2 as cv
import numpy as np
from PIL import Image

from chapter_module import ChapterModule


class BasicImageEnhancementsChapter(ChapterModule):

    def __init__(self, config):
        super().__init__(config)

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

        # cv.imwrite(str(self.assetsDirectory / 'Piano_Sheet_Music_thresh.png'), sheetMusicAdaptiveThresholdedImg)

        # print(buildingImg.shape, buildingImg.dtype)
        # print(maskImg.shape, maskImg.dtype)
        return (
            Image.fromarray(sheetMusicImg, mode='L'),
            Image.fromarray(sheetMusicThresholdedImg, mode='L'),
            Image.fromarray(sheetMusicAdaptiveThresholdedImg, mode='L')
        )

    def bitwiseSampleImages(self):
        circleImagePath = self.assetsDirectory / 'circle.jpg'
        if not circleImagePath.exists():
            print(f'[E] Path not exists: {str(circleImagePath)}')
            return ()

        rectangleImagePath = self.assetsDirectory / 'rectangle.jpg'
        if not rectangleImagePath.exists():
            print(f'[E] Path not exists: {str(rectangleImagePath)}')
            return ()

        circleImage = cv.imread(str(circleImagePath), cv.IMREAD_GRAYSCALE)
        rectangleImage = cv.imread(str(rectangleImagePath), cv.IMREAD_GRAYSCALE)

        return (
            Image.fromarray(circleImage, mode='L'),
            Image.fromarray(rectangleImage, mode='L')
        )

    def simpleBitwiseOperations(self):
        circleImagePath = self.assetsDirectory / 'circle.jpg'
        if not circleImagePath.exists():
            print(f'[E] Path not exists: {str(circleImagePath)}')
            return ()

        rectangleImagePath = self.assetsDirectory / 'rectangle.jpg'
        if not rectangleImagePath.exists():
            print(f'[E] Path not exists: {str(rectangleImagePath)}')
            return ()

        circleImage = cv.imread(str(circleImagePath), cv.IMREAD_GRAYSCALE)
        rectangleImage = cv.imread(str(rectangleImagePath), cv.IMREAD_GRAYSCALE)

        andImageResult = cv.bitwise_and(circleImage, rectangleImage)
        orImageResult = cv.bitwise_or(circleImage, rectangleImage)
        xorImageResult = cv.bitwise_xor(circleImage, rectangleImage)

        return (
            Image.fromarray(andImageResult, mode='L'),
            Image.fromarray(orImageResult, mode='L'),
            Image.fromarray(xorImageResult, mode='L'),
        )

    def cokeAndMosaic(self):

        cokeImagePath = self.assetsDirectory / 'coca-cola-logo.png'
        if not cokeImagePath.exists():
            print(f'[E] Path not exists: {str(cokeImagePath)}')
            return ()

        mosaicImagePath = self.assetsDirectory / 'checkerboard_color.png'
        if not mosaicImagePath.exists():
            print(f'[E] Path not exists: {str(mosaicImagePath)}')
            return ()

        cokeImage = cv.imread(str(cokeImagePath), cv.IMREAD_COLOR)
        mosaicImage = cv.imread(str(mosaicImagePath), cv.IMREAD_COLOR)

        return (
            Image.fromarray(cokeImage[:, :, ::-1], mode='RGB'),
            Image.fromarray(mosaicImage[:, :, ::-1], mode='RGB'),
        )

    def task(self):

        cokeImagePath = self.assetsDirectory / 'coca-cola-logo.png'
        if not cokeImagePath.exists():
            print(f'[E] Path not exists: {str(cokeImagePath)}')
            return ()

        mosaicImagePath = self.assetsDirectory / 'checkerboard_color.png'
        if not mosaicImagePath.exists():
            print(f'[E] Path not exists: {str(mosaicImagePath)}')
            return ()

        cokeImage = cv.imread(str(cokeImagePath), cv.IMREAD_COLOR)
        mosaicImage = cv.imread(str(mosaicImagePath), cv.IMREAD_COLOR)

        dims = (cokeImage.shape[0], cokeImage.shape[1])
        mosaicResizedImage = cv.resize(mosaicImage, dims)

        cokeMonoImage = cv.cvtColor(cokeImage, cv.COLOR_BGR2GRAY)
        _, cokeTextMask = cv.threshold(cokeMonoImage, 200, 255, cv.THRESH_BINARY)
        _, cokeBackMask = cv.threshold(cokeMonoImage, 200, 255, cv.THRESH_BINARY_INV)

        mosaicOnTextImage = cv.bitwise_and(mosaicResizedImage, mosaicResizedImage, mask=cokeTextMask)

        cokeBackOnlyImage = cv.bitwise_and(cokeImage, cokeImage, mask=cokeBackMask)

        resultImage = cv.bitwise_or(mosaicOnTextImage, cokeBackOnlyImage)

        return (
            Image.fromarray(mosaicOnTextImage[:, :, ::-1], mode='RGB'),
            Image.fromarray(cokeBackOnlyImage[:, :, ::-1], mode='RGB'),
            Image.fromarray(resultImage[:, :, ::-1], mode='RGB'),
            # Image.fromarray(cokeMonoImage, mode='L'),
            # Image.fromarray(cokeTextMask, mode='L'),
            # Image.fromarray(cokeBackMask, mode='L'),
        )

    def work(self):
        return (
            self.imageAddition(),
            self.imageMultiplication(),
            self.thresholdSimple(),
            self.thresholdSheetMusic(),
            self.bitwiseSampleImages(),
            self.simpleBitwiseOperations(),
            self.cokeAndMosaic(),
            self.task(),
        )


################################################################################
def classFactory(config):

    return BasicImageEnhancementsChapter(config)
