#LNM Hacks 4.0
#Anubhav Natani

#imports
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
from scipy.spatial import distance
import scipy

#variables
embedder = FaceNet()
detector = MTCNN()


#reconcilation of the code
def get_face_image(image):
  data = plt.imread(image)
  faces = detector.detect_faces(data)
  #getting one face only can be extended to more then one face easily
  #corrdinateds fo the first face
  x1, y1, width, height = faces[0]['box']
  x1, y1 = abs(x1), abs(y1)
  x2, y2 = x1 + width, y1 + height
  new_data = data[y1:y2, x1:x2]
  #resizing the data
  r_data = cv2.resize(new_data, (160,160), interpolation=cv2.INTER_CUBIC)
  return r_data

def get_embeddings(img):
  embeddings = embedder.embeddings([img])
  return embeddings

def calc_dist(a_e, b_e):
    return distance.euclidean(a_e, b_e)

def get_match_score(dist):
  #different thershold can be selected
  if(dist>1):
    return 0
  else:
    return 1

