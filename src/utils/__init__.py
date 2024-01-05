from pathlib import Path
from zipfile import ZipFile
from urllib.request import urlretrieve


################################################################################
def downloadAndUnzip(url, save_path):
    print('Downloading and extracting assets...', end='')

    filename, headers = urlretrieve(url, save_path)
    print(filename)

    try:
        with ZipFile(save_path) as z:
            z.extractall(Path(save_path).absolute().parent)

        print('Done')

    except Exception as e:
        print('\nInvalid file.', e)

