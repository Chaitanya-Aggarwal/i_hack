# import required packages
import cv2
import dlib
import time
import os

INPUT_PATH = "ImageData/"
OUTPUT_PHOTO_PATH = "PhotoGraphData/"
OUTPUT_BLANK_PATH = "DocumentData/"
WEIGHTS = "./mmod_human_face_detector.dat"

inputData = os.listdir(INPUT_PATH)
print("The input image files are")
print(inputData)

# load the photograph
for i in inputData:
    # load input image
    image = cv2.imread(INPUT_PATH+i)

    if image is None:
        print("Could not read input image")
        exit()

    # initialize hog + svm based face detector
    hog_face_detector = dlib.get_frontal_face_detector()

    # initialize cnn based face detector with the weights
    # cnn_face_detector = dlib.cnn_face_detection_model_v1(WEIGHTS)

    start = time.time()
    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    for k in range(4):
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        # apply face detection (hog)
        faces_hog = hog_face_detector(image, 1)
        if ( faces_hog ):
            break

    end = time.time()
    print("Execution Time (in seconds) :")
    print("HOG : ", format(end - start, '.2f'))

    if not (faces_hog):
        cv2.imwrite(OUTPUT_BLANK_PATH+i+"_dlib.jpg", image)
        continue
    # loop over detected faces
    for face in faces_hog:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y

        # draw box over face
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)


    start = time.time()

    # apply face detection (cnn)
    # faces_cnn = cnn_face_detector(image, 1)

    # end = time.time()
    # print("CNN : ", format(end - start, '.2f'))

    # # loop over detected faces
    # for face in faces_cnn:
    #     x = face.rect.left()
    #     y = face.rect.top()
    #     w = face.rect.right() - x
    #     h = face.rect.bottom() - y

    #      # draw box over face
    #     cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

    # write at the top left corner of the image
    # for color identification
    img_height, img_width = image.shape[:2]
    cv2.putText(image, "HOG", (img_width-50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0,255,0), 2)
    # cv2.putText(image, "CNN", (img_width-50,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
    #                 (0,0,255), 2)

    # display output image
    # cv2.imshow("face detection with dlib", image)
    # cv2.waitKey()

    # save output image 
    cv2.imwrite(OUTPUT_PHOTO_PATH+i+"_dlib.jpg", image)

    # close all windows
    cv2.destroyAllWindows()
