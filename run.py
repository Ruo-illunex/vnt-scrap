import re
import os
import requests
from io import BytesIO

from PIL import Image
import pytesseract

from src import settings, utils

# 이미지 URL
url = settings.captcha_img_url

# requests를 사용하여 이미지를 가져옵니다
response = requests.get(url)

# 이미지가 정상적으로 다운로드 되었는지 확인
if response.status_code == 200:
    # 결과를 저장할 폴더를 생성합니다.
    folder_name = utils.get_current_time()
    folder_path = os.path.join('results', 'result-pytesseract', folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # BytesIO를 사용하여 이미지 데이터를 메모리에 로드합니다
    image = Image.open(BytesIO(response.content))

    # 이미지를 파일로 저장합니다
    image_path = f'results/result-pytesseract/{folder_name}/captcha_img_{folder_name}.png'
    image.save(image_path)

    utils.preprocess_image(image_path, folder_name) # 이미지 전처리

    # 전처리된 이미지를 다시 불러옵니다
    preprocessed_image = Image.open(f'results/result-pytesseract/{folder_name}/preprocessed_image.png')

    # OCR Engine Mode(–oem)과 Page Segmentation Mode(–psm)을 설정합니다
    # --psm N
    # Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:
    # 0 = Orientation and script detection (OSD) only.
    # 1 = Automatic page segmentation with OSD.
    # 2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
    # 3 = Fully automatic page segmentation, but no OSD. (Default)
    # 4 = Assume a single column of text of variable sizes.
    # 5 = Assume a single uniform block of vertically aligned text.
    # 6 = Assume a single uniform block of text.
    # 7 = Treat the image as a single text line.
    # 8 = Treat the image as a single word.
    # 9 = Treat the image as a single word in a circle.
    # 10 = Treat the image as a single character.
    # 11 = Sparse text. Find as much text as possible in no particular order.
    # 12 = Sparse text with OSD.
    # 13 = Raw line. Treat the image as a single text line,
    #     bypassing hacks that are Tesseract-specific.

    # --oem N
    # Specify OCR Engine mode. The options for N are:
    # 0 = Original Tesseract only.
    # 1 = Neural nets LSTM only.
    # 2 = Tesseract + LSTM.
    # 3 = Default, based on what is available.
    config = ('--oem 3 --psm 6')

    # pytesseract를 사용하여 저장된 이미지에서 텍스트를 추출합니다
    text = pytesseract.image_to_string(preprocessed_image, config=config)
    print(f'OCR 결과 : {text}')
    print(f'Length: {len(text)}')

    numbers = re.findall(r'\d+', text)
    print(f'OCR 결과(숫자만) : {numbers}')

    # 추출한 텍스트를 파일로 저장합니다
    result_path = f'results/result-pytesseract/{folder_name}/result_{folder_name}.txt'
    utils.save_to_file(result_path, text)
else:
    print("이미지를 다운로드할 수 없습니다.")
