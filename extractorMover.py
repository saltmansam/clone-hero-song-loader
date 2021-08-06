import zipfile
from pyunpack import Archive
import os


def extractFiles(path_to_zip_file = "", directory_to_extract_to = ""):
    folderName = ""
    filePath = path_to_zip_file
    print(filePath)

    #FIXME
    # for index, char in enumerate(filePath):
    #     if char == '/':
    #         filePath = filePath[index:]
    #     if filePath.find('/') == -1:
    #         folderName = filePath
    #         print(folderName)
    #         break

    directory = os.path.join(directory_to_extract_to) # + "/" + folderName)
    if not os.path.exists(directory):
        os.mkdir(directory)

    try:
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory)
    except Exception:
        Archive(path_to_zip_file).extractall(directory)