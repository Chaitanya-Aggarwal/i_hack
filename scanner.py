from imutils.perspective import four_point_transform
import cv2

INPUT_PATH = "ImageData/"

height = 800
width = 600
green = (0, 255, 0)

image = cv2.imread(INPUT_PATH+"input/2.jpg")
image = cv2.resize(image, (width, height))
orig_image = image.copy()
