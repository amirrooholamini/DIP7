import numpy as np
import cv2
import os

folder_path = 'outputs/section_3'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

image_names = [
    'xray_noisy.png',
    'Medianfilterp.png',
    'image_noisy.png',
    'board_noisy.png',
    'balloons_noisy.png',
    '5.png'
    ]

for name in image_names:
    full_path = f"resources/{name}"
    image = cv2.imread(full_path)

    median_image = cv2.medianBlur(image, 7)

    cv2.imwrite(f'{folder_path}/{name.replace(".png", "")}_median_applied.png', median_image)