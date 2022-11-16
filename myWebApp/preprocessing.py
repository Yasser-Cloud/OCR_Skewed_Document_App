from skimage.transform import hough_line, hough_line_peaks, rotate
from skimage.feature import canny
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from scipy.stats import mode
import numpy as np
from PIL import Image
import cv2
import pytesseract
from pytesseract import image_to_string
from pytesseract import Output

def imageCorrection(fixed_angle, image):
    fixed_image = rotate(image, fixed_angle)
    imsave('./fixed_image.png',fixed_image)

def Hough_Transform(image_path):

    # Use canny edge detector
    image = imread(image_path)
    edges = canny(image)

    # Classic straight-line Hough transform
    # Note that the maximum skewed angel 5 degree so we choose angel here between 90 + 6 and 90 - 6 degree
    # That make Algorithm run faster and make a better result
    tested_angles = np.deg2rad(np.arange(84.0, 96.0))
    h, theta, d = hough_line(edges, theta=tested_angles)

    _, angles,_ =hough_line_peaks(h, theta, d)

    angle = np.rad2deg(mode(angles)[0][0])
    #Choosing angle using vote
    fixed_angle = -(90 - angle)
    imageCorrection(fixed_angle, image)





def OCR():
    img = cv2.imread(r'fixed_image.png')

    h, w, c = img.shape


    custom_config = r'--oem 3 --psm 6'

    d = pytesseract.image_to_data(img, output_type=Output.DICT, config= custom_config)

    res =[]
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            res.append(d['text'][i])
    #print('Words with more than 60% confident: ')
    #print(res)

    disp_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite('static/After_Rotation.png',disp_img)
    return res
