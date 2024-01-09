from chapter_module import ChapterModule


class VideoCaptureChapter(ChapterModule):

    def __init__(self, config):
        super().__init__(config)

    def work():
        pass


def classFactory(config):
    return VideoCaptureChapter(config)
