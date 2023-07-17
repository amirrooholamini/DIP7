import numpy as np
import cv2
import os

folder_path = 'outputs/section_4_b'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

image = cv2.imread("resources/tsukuba_l.png", cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)
clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(5, 5))
clahe_image = clahe.apply(image)

cv2.imshow("not good image", equalized_image)
cv2.imshow("good image", clahe_image)
cv2.waitKey()

cv2.imwrite(f"{folder_path}/equalized_image.png", equalized_image)
cv2.imwrite(f"{folder_path}/clahe.png", clahe_image)
