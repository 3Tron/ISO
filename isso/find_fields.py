
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import sys
from os import listdir
from os.path import isfile, join

class FindFields:

    def __init__(self):
        self.start_data = 'test'

    def is_greenish(self,clr, level=-1):
        r, g, b = clr
        if (g > r and g > b):
            return True
        return False


    def find_fielding(self, infile, outfile, numcolors=5, swatchsize=20, resize=96):
        image = Image.open(infile)
        image = image.resize((resize, resize))
        result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
        result.putalpha(0)
        colors = result.getcolors(resize * resize)

        # Save colors to file
        greenscore = 0
        clrs = result.getcolors()
        for i in range(5):
            r, g, b, a = clrs[i][1]
            if(self.is_greenish((r, g, b), i)):
                greenscore += 1
        print(infile, greenscore, result.getcolors()[:5])

        if greenscore > 3:
            pal = Image.new('RGB', (swatchsize * numcolors, swatchsize * 3))
            draw = ImageDraw.Draw(pal)
            #get_avg(infile)

            posx = 0
            for count, col in colors:
                draw.rectangle([posx, 0, posx + swatchsize,
                                swatchsize * 3], fill=col)
                posx = posx + swatchsize

            del draw
            pal.save(outfile, "PNG")


def main():
    # for arg in sys.argv[1:]:
    #    print(arg)

    mypath = sys.argv[1]
    ff = FindFields()
    if isfile(mypath):
        ff.find_fielding(f, f + 'out.png')
    else:
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for f in onlyfiles:
            if 'out' not in f:
                ff.find_fielding(f, f + 'out.png')


if __name__ == "__main__":
    main()
