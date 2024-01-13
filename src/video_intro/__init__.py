import cv2
from chapter_module import ChapterModule

class VideoIntroChapter(ChapterModule):
    cv2WindowName = 'Camera Preview'
    videoSourceIndex = 0

    def __init__(self, config):
        super().__init__(config)

    def init(self):
        self.videoSource = cv2.VideoCapture()
        self.videoSource.open(self.videoSourceIndex)
        isOpened = self.videoSource.isOpened()
        # print('can open', canOpen, 'is opened:', isOpened)
        if not isOpened:
            raise Exception(f'can not open video source {self.videoSourceIndex}')

        cv2.namedWindow(self.cv2WindowName)

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

    return VideoIntroChapter(config)
