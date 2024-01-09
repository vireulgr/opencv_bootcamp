from pathlib import Path
from utils import downloadAndUnzip


class ChapterModule(object):

    def __init__(self, config):
        self.configObject = config
        self.assetsDirectory = Path(self.configObject['assetsDir'])
        self.assetsDirectory.mkdir(parents=True, exist_ok=True)

        assetsZipPath = self.assetsDirectory / self.configObject['resourcesFileName']

        # print(assetsZipPath)
        if not assetsZipPath.exists():
            downloadAndUnzip(self.configObject['resourcesUrl'], assetsZipPath)
        # print('chapter module ctor out')

