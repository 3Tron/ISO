
from find_fields import FindFields
import sys
from os import listdir
from os.path import isfile, join


def main():
    # for arg in sys.argv[1:]:
    #    print(arg)

    inputPath = sys.argv[1]

    ff = FindFields()
    if isfile(inputPath):
        ff.find_fielding(inputPath, inputPath + 'out.png')
    else:
        onlyfiles = [f for f in listdir(
            inputPath) if isfile(join(inputPath, f))]
        for f in onlyfiles:
            if 'out' not in f:
                ff.find_fielding(inputPath + "/" + f,
                                 inputPath + "/" + f + 'out.png')


if __name__ == "__main__":
    main()
