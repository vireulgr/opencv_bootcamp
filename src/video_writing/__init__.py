import cv2
from chapter_module import ChapterModule
from pathlib import Path

class VideoWritingChapter(ChapterModule):
    cv2WindowName = 'Camera Preview'

    def __init__(self, config):
        super().__init__(config)
        self.videoSourceName = Path(self.assetsDirectory) / 'race_car.mp4'
        self.videoSource = cv2.VideoCapture()
        outDirectory = Path(self.assetsDirectory) / 'out'
        outDirectory.mkdir(parents=True, exist_ok=True)

        self.videoFileName1 = outDirectory / 'race_car_out.avi'
        self.videoFileName2 = outDirectory / 'race_car_out.mp4'

    def init(self):
        if not self.videoSourceName.is_file():
            raise Exception(f'{self.videoSourceName} is not a file!')

        self.videoSource.open(self.videoSourceName.as_posix())
        isOpened = self.videoSource.isOpened()
        # print('can open', canOpen, 'is opened:', isOpened)
        if not isOpened:
            raise Exception(f'can not open video source {self.videoSourceName}')

        cv2.namedWindow(self.cv2WindowName)

    def writeToDisk(self):

        frameWidth = int(self.videoSource.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(self.videoSource.get(cv2.CAP_PROP_FRAME_HEIGHT))
        videoFps = int(self.videoSource.get(cv2.CAP_PROP_FPS))
        totalFrames = int(self.videoSource.get(cv2.CAP_PROP_FRAME_COUNT))
        # print(f'w {frameWidth} h {frameHeight} fps {videoFps}')
        outAvi = cv2.VideoWriter(self.videoFileName1.as_posix(), cv2.VideoWriter_fourcc(*'MJPG'), videoFps, (frameWidth, frameHeight))
        outMp4 = cv2.VideoWriter(self.videoFileName2.as_posix(), cv2.VideoWriter_fourcc(*'XVID'), videoFps, (frameWidth, frameHeight))

        curFrameNumber = 0
        while True:
            res, frame = self.videoSource.read()
            if not res:
                break

            def compareToPoints(p):
                thresh = 0.005
                points = [0, 0.25, 0.5, 0.75, 1.0]
                result = False
                for item in points:
                    if abs(p - thresh) > item:
                        continue
                    result = result or (abs(p - item) <= thresh)
                    if result:
                        break
                return result

            progress = curFrameNumber / totalFrames
            if compareToPoints(progress):
                print(f'progress is {int(progress * 100)}%')

            outAvi.write(frame)
            outMp4.write(frame)
            curFrameNumber += 1

        outAvi.release()
        outMp4.release()

    def show(self):
        while cv2.waitKey(1) != 27:
            hasFrame, frame = self.videoSource.read()
            if not hasFrame:
                print('not has frame')
                break
            cv2.imshow(self.cv2WindowName, frame)

    def cleanup(self):
        self.videoSource.release()
        cv2.destroyAllWindows()

def classFactory(config):

    return VideoWritingChapter(config)
