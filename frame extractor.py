import cv2
import os
path = 'Blue Lid/'
count = 0
for files in os.listdir(path):
    print(files)
    vidcap = cv2.VideoCapture(path+files)
    success, image = vidcap.read()

    while success:
      cv2.imwrite("{file_path}/frame{count}.jpg".format(file_path=path, count=count), image)     # save frame as JPEG file
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
