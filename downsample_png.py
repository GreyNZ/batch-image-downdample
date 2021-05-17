import cv2
import numpy as np
import matplotlib.pyplot as plt
import itertools

OPEN_PATH = "PNG/"
SAVE_PATH = "PNG_SMOL/"

FILE_PREFIX = "IMG_"
FILE_SUFFIX = ".png"

START = 1266 # starting image tag
END = 1660   # final image tag

DOWNSAMPLE = 2

MISSING_IMAGES = [] #basic log for missing images


def downsample_image(img, downsample=1):
    """takes an image and and positive integer,
    downsamples image integer times and returns it"""
    for _ in itertools.repeat(None, downsample):
        img = cv2.pyrDown(img) 
    return img

#def open_img(file):
#    """trys to open image, if successful returns img, else retrusn False"""
#    try:
#        img = cv2.imread(f'{OPEN_PATH}{FILE_PREFIX}{file}{FILE_SUFFIX}')
#        return img
#    except:
#        return False

def main():
    for i in range(START,END):
        img = cv2.imread(f'{OPEN_PATH}{FILE_PREFIX}{i}{FILE_SUFFIX}')
        if img is not None:
            img = downsample_image(img, downsample=DOWNSAMPLE)
            cv2.imwrite(f'{SAVE_PATH}{FILE_PREFIX}{i}{FILE_SUFFIX}', img)
        else:
            MISSING_IMAGES.append(f'{FILE_PREFIX}{i}{FILE_SUFFIX}: was missing or unreadable')
    for i in MISSING_IMAGES:
        print(i)

main()



