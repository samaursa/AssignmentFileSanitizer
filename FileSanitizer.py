import os
import re
import sys

dirToWalk = "."
if len(sys.argv) == 2:
    dirToWalk = sys.argv[1]

if os.path.isdir(dirToWalk) is False:
    print('Directory "{0}" does not exist'.format(dirToWalk))
    exit()

p = re.compile('100[0-9]{6}')
for root, dirs, files in os.walk(dirToWalk):
    for file in files:
        for itr in p.finditer(file):
            m = next(p.finditer(file))
            newFileName = file[m.start():m.end()]
            _, ext = os.path.splitext(file)

            oldFilePath = root + "/" + file
            newFilePath = root + "/" + newFileName + ext

            print(oldFilePath)

            if oldFilePath == newFilePath:
                continue

            if os.path.isfile(newFilePath):
                print("File {} already exists. Rename FAILED.".format(newFilePath))
                continue

            os.rename(oldFilePath, newFilePath)

            print("Renamed {} to {}".format(oldFilePath, newFilePath))
            break
    break
