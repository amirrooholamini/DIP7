import numpy as np
import cv2
import os

kernel_1 = np.ones((5,5)) * 0.04
kernel_2 = np.ones((5,5)) * 1
kernel_3 = np.ones((5,5)) * 5
kernel_4 = np.ones((3,3)) * 0.04
kernel_5 = np.ones((3,3)) * 1
kernel_6 = np.ones((3,3)) * 5

image = cv2.imread("resources/1.tif", cv2.IMREAD_GRAYSCALE)

result_1 = cv2.filter2D(image, -1, kernel_1)
result_2 = cv2.filter2D(image, -1, kernel_2)
result_3 = cv2.filter2D(image, -1, kernel_3)
result_4 = cv2.filter2D(image, -1, kernel_4)
result_5 = cv2.filter2D(image, -1, kernel_5)
result_6 = cv2.filter2D(image, -1, kernel_6)

results = np.hstack((result_1, result_2, result_3, result_4, result_5, result_6))
folder_path = 'outputs/section_2'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

cv2.imwrite(f"{folder_path}/results.jpg", results)
