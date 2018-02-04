import cv2
import numpy

def get_avg(f):
    myimg = cv2.imread(f)
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    #print(f, avg_color)
    return avg_color
