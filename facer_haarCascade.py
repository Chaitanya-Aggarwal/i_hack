# example of face detection with opencv cascade classifier
from cv2 import imread
from cv2 import CascadeClassifier
from cv2 import rectangle
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
import os

INPUT_PATH = "InputDatas/"

if __name__=="__main__":
    inputData = os.listdir(INPUT_PATH)
    cnt = 0
    print(str(inputData))
    # load the photograph
    for i in inputData:
        pixels = imread(INPUT_PATH+i)
        # load the pre-trained model
        classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
        # perform face detection
        bboxes = classifier.detectMultiScale(pixels)
        # print bounding box for each detected face
        for box in bboxes:
            print(box)

        # extract
        x, y, width, height = box
        if ( width <= 1 or height <= 1 ):
            cnt +=1 
        x2, y2 = x + width, y + height
        # draw a rectangle over the pixels
        rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)

        # show the image
        imshow('face detection', pixels)
        # keep the window open until we press a key
        waitKey(0)
        # close the window
        destroyAllWindows()  
    print (cnt)                                                     