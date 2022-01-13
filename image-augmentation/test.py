import numpy as np
from transformations.flip import flipImage
from os import listdir
from transformations.noise import noiseImage
from transformations.rotate import rotateImage
from transformations.zoom import zoomImage
from utils.drawBoxes import drawBoxes
from utils.getImageAndLabels import getImageAndLabels
from utils.plotImages import plotImages
import cv2

def flipTest(image , labels):

    img1 = drawBoxes(*flipImage(image, labels, 1))
    img2 = drawBoxes(*flipImage(image, labels, 0))
    img3 = drawBoxes(*flipImage(image, labels, -1))
    imgT = drawBoxes(*flipImage(image, labels, 2))

    plotList = [imgT, img1, img2, img3]
    titleList = ['Ground True', 'Horizomtal flip', 'Vertical flip',  'Both flip']

    plotImages(plotList, titleList)

def rotateTest(image , labels):

    img1 = drawBoxes(*rotateImage( image, labels, 1))
    img2 = drawBoxes(*rotateImage( image, labels, 2))
    img3 = drawBoxes(*rotateImage( image, labels, 3))
    imgT = drawBoxes(*rotateImage( image, labels, 0))

    plotList = [imgT, img1, img2, img3]
    titleList = ['Ground True', '90º', '180º',  '270º']

    plotImages(plotList, titleList)

def rotateFlipTest(image, labels):

    rotateTitles = ['Ground True', '90º', '180º',  '270º']
    flipTitles = ['Ground True', 'Horizomtal flip', 'Vertical flip',  'Both flip']
    rotateCodes = [0, 1, 2, 3]
    flipCodes = [2, 1, 0, -1]

    plotList = []
    titleList = []

    for rotCode, rotTitle in zip(rotateCodes, rotateTitles):
        for flipCode, flipTitle in zip(flipCodes, flipTitles):
            img, new_labels = rotateImage(image, labels, rotCode)
            img, new_labels = flipImage(img, new_labels, flipCode)
            img = drawBoxes(img, new_labels)
            new_title = rotTitle + " " + flipTitle
            plotList.append(img)
            titleList.append(new_title)

    plotImages(plotList, titleList, len(flipCodes), len(rotateCodes))


def zoomTest(image , labels):

    img1 = drawBoxes(*zoomImage( image, labels, 1, 1.5))
    img2 = drawBoxes(*zoomImage( image, labels, 1.5, 1))
    img3 = drawBoxes(*zoomImage( image, labels, 2, 2))
    imgT = drawBoxes(*zoomImage( image, labels, 1, 1))

    plotList = [imgT, img1, img2, img3]
    titleList = ['Ground True', 'W = 1, H = 1.5', 'W = 1.5, H = 1',  'W = 2, H = 2']

    plotImages(plotList, titleList)

imagesPath = "./test-images/"
imagesList = [f for f in listdir(imagesPath) if (f.endswith('.png') or f.endswith('.jpg')) ]

def noiseTest(image):

    imgT = noiseImage( image.copy(), percent=0)
    img1 = noiseImage( image.copy(), size= (3,3))
    img2 = noiseImage( image.copy(), percent=0.5, size = (5,1))
    img3 = noiseImage( image.copy(), percent=0.5, size=(10,10))

    plotList = [imgT, img1, img2, img3]
    titleList = ['Ground True', 'Percent = 0,1%  noiseSize = (1,1)', 
                'Percent = 0,5%  noiseSize = (1,1)',  'Percent = 0,5%  noiseSize = (2,2)']

    plotImages(plotList, titleList)

imagesPath = "./test-images/"
imagesList = [f for f in listdir(imagesPath) if (f.endswith('.png') or f.endswith('.jpg')) ]



for image in imagesList:
    image, labels = getImageAndLabels(image, imagesPath)
    #rotateTest(image, new_labels)
    #rotateFlipTest(image, new_labels)
    #zoomTest( image, labels)
    noiseTest(image)

        
