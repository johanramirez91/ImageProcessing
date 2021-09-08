# You must install the following libraries:
import cv2
from math import pi
import numpy as np

class Roundness():
    '''
    initialize the class and set the class attributes
    '''

    def __init__(self, image_path):
        self._img1 = None
        self._img2 = None
        self._img_path = image_path

    def load_image(self):
        self._img1 = cv2.imread("SampleImage1.jpg")  # sample image1 to test the code
        self._img2 = cv2.imread("SampleImage2.jpg")  # sample image2 to test the code
        cv2.imshow("Circle 1", self._img1)
        cv2.imshow("Circle 2", self._img2)
        id.processing_image()

    def processing_image(self):
        imGray = cv2.cvtColor(self._img2, cv2.COLOR_BGR2GRAY)
        im_gauss = cv2.GaussianBlur(imGray, (5, 5), 0)
        ret, thresh = cv2.threshold(im_gauss, 127, 255, 0)
        # Get contours
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_circles = []
        for con in contours:
            perimeter = cv2.arcLength(con, True)
            area = cv2.contourArea(con)
            circularity = 4 * pi * (area / (perimeter * perimeter))
        print("Roundness: ", circularity)

    def start_detection(self):
        self.load_image()
        cv2.waitKey(0)
        cv2.destroyAllWindows()


id = Roundness(r'C:\Users\USER\PythonProjects\ImageProcessing')
id.start_detection()


