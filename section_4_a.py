import numpy as np
import cv2
import os

folder_path = 'outputs/section_4_a'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

image_names = [
    'Unequalized_Hawkes_Bay_NZ.jpg',
    '4.png',
    ]

for name in image_names:
    full_path = f"resources/{name}"
    image = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
    equalized_image = cv2.equalizeHist(image)
    cv2.imwrite(f'{folder_path}/{name.split(".")[0]}_equalized.png', equalized_image)
