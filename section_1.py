import numpy as np
import cv2
import os

# 1. Edge detection filter
kernel_1 = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel_2 = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel_3 = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel_4 = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 5. Your filter (emboss 2)
kernel_5 = np.array([[-2  ,  -1 ,  0],
                   [-1  ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 6. Your filter (sharpening 2)
kernel_6 = np.array([[-1  ,  -1 , -1],
                   [-1  ,  9 ,  -1],
                   [-1  ,  -1 ,  -1]])

# 7. Your filter (sharpening 2)
kernel_7 = np.ones((8,8)) / 64

image = cv2.imread("resources/me.jpg", cv2.IMREAD_GRAYSCALE)

if1 = cv2.filter2D(image, -1, kernel_1)
if2 = cv2.filter2D(image, -1, kernel_2)
if3 = cv2.filter2D(image, -1, kernel_3)
if4 = cv2.filter2D(image, -1, kernel_4)
if5 = cv2.filter2D(image, -1, kernel_5)
if6 = cv2.filter2D(image, -1, kernel_6)
if7 = cv2.filter2D(image, -1, kernel_7)

result_1 = np.hstack((image, if1))
result_2 = np.hstack((image, if2))
result_3 = np.hstack((image, if3))
result_4 = np.hstack((image, if4))
result_5 = np.hstack((image, if5))
result_6 = np.hstack((image, if6))
result_7 = np.hstack((image, if7))

folder_path = 'outputs/section_1'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

cv2.imwrite(f"{folder_path}/if1.jpg", result_1)
cv2.imwrite(f"{folder_path}/if2.jpg", result_2)
cv2.imwrite(f"{folder_path}/if3.jpg", result_3)
cv2.imwrite(f"{folder_path}/if4.jpg", result_4)
cv2.imwrite(f"{folder_path}/if5.jpg", result_5)
cv2.imwrite(f"{folder_path}/if6.jpg", result_6)
cv2.imwrite(f"{folder_path}/if7.jpg", result_7)