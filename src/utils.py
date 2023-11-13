import time

import cv2
from PIL import Image, ImageEnhance
import numpy as np


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def save_to_file(filename, result_text):
    with open(filename, 'w') as f:
        f.write(result_text)


def preprocess_image(image_path, folder_name):
    # 이미지를 불러옵니다
    image = cv2.imread(image_path)

    # 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이진화
    # cv2.threshold를 사용하여 이진화를 적용할 수 있습니다.
    # 여기서는 adaptiveThreshold를 사용하여 이미지의 다양한 영역에서 다르게 이진화를 적용합니다.
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 노이즈 제거
    # 노이즈를 제거하기 위해 medianBlur를 사용할 수 있습니다.
    denoise = cv2.medianBlur(thresh, 3)

    # 대비 향상
    # Pillow의 ImageEnhance 기능을 사용하여 대비를 조절합니다.
    contrast = ImageEnhance.Contrast(Image.fromarray(denoise))
    high_contrast = contrast.enhance(2)

    # 이미지 저장
    high_contrast.save(f'results/result-pytesseract/{folder_name}/preprocessed_image.png')
