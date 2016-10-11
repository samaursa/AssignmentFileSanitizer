import os
import re

for root, dirs, files in os.walk("../"):
    for file in files:
        p = re.compile('100[0-9]{6}')
        m = next(p.finditer(file))
        newFileName = file[m.start():m.end()]
        _, ext = os.path.splitext(file)

        oldFilePath = root + file
        newFilePath = root + newFileName + ext

        if (oldFilePath == newFilePath):
            continue

        os.rename(oldFilePath, newFilePath)

        print("Renamed {} to {}".format(oldFilePath, newFilePath))
    break
