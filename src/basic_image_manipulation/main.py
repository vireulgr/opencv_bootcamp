import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve


def download_and_unzip(url, save_path):
    print('Downloading and extracting assets...', end='')

    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])

        print('Done')

    except Exception as e:
        print('\nInvalid file.', e)


URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), 'opencv_bootcamp_assets_NB1.zip')

image_assets_directory = os.path.join(os.getcwd(), 'assets', 'img')

# print(image_assets_directory)

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

imgNewZealandLakeBGR = cv.imread('New_Zealand_Lake.jpg', cv.IMREAD_COLOR)
#imgTmp = cv.imread(os.path.join(image_assets_directory, 'checkerboard_18x18.png'))

#imgTmpGrayscale = cv.imread('checkerboard_18x18.png', cv.IMREAD_GRAYSCALE)
#print(imgTmpGrayscale)

#fig, ax = plt.subplots()
#im = ax.imshow(imgTmp)

#ax.axis('off')
#plt.show()

#imgTmp = cv.imread('checkerboard_84x84.jpg')

#im = ax.imshow(imgTmp)
#plt.show()


# imgTmp = cv.imread('coca-cola-logo.png', cv.IMREAD_COLOR)
################################################################################
# imgTmp = cv.imread('New_Zealand_Lake.jpg', cv.IMREAD_COLOR)

b, g, r = cv.split(imgNewZealandLakeBGR)

plt.figure(figsize=[16, 16])
plt.subplot(241); plt.imshow(r, cmap='gray'); plt.title('Red channel')
plt.subplot(242); plt.imshow(g, cmap='gray'); plt.title('Green channel')
plt.subplot(243); plt.imshow(b, cmap='gray'); plt.title('Blue channel')

imgMerged = cv.merge((b, g, r))

plt.subplot(244); plt.imshow(imgMerged[:, :, ::-1]); plt.title('Merged output')

#plt.show()

################################################################################

imgNewZealandLakeRGB = cv.cvtColor(imgNewZealandLakeBGR, cv.COLOR_BGR2RGB)
#fig, ax = plt.subplots()
#im = ax.imshow(imgTmpConverted)
#plt.show()
################################################################################

# imgTmp = cv.imread('New_Zealand_Lake.jpg', cv.IMREAD_COLOR)
imgNewZealandLakeHSV = cv.cvtColor(imgNewZealandLakeBGR, cv.COLOR_BGR2HSV)

h, s, v = cv.split(imgNewZealandLakeHSV)

cv.rectangle(imgNewZealandLakeRGB, (50, 50), (100, 100), (125, 255, 255), 5)

#plt.figure(figsize=[16, 8])
plt.subplot(245); plt.imshow(h, cmap='gray'); plt.title('Hue')
plt.subplot(246); plt.imshow(s, cmap='gray'); plt.title('Saturation')
plt.subplot(247); plt.imshow(v, cmap='gray'); plt.title('Luminance')

plt.subplot(248); plt.imshow(imgNewZealandLakeRGB); plt.title('Original')

plt.show()
################################################################################

imgTmpBGR = cv.imread(os.path.join(image_assets_directory, 'New_Zealand_Lake.jpg'), cv.IMREAD_COLOR)
cv.imwrite('New_Zealand_Lake_SAVED.png', imgTmpBGR)

