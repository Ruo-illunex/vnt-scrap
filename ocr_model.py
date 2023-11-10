import os
from io import BytesIO

import requests
from PIL import Image
from model.model import process_and_predict

from src import settings, utils


# 이미지 URL
url = settings.captcha_img_url

# requests를 사용하여 이미지를 가져옵니다
response = requests.get(url)

# 이미지가 정상적으로 다운로드 되었는지 확인
if response.status_code == 200:
    # 결과를 저장할 폴더를 생성합니다.
    folder_name = utils.get_current_time()
    folder_path = os.path.join('results', 'result-keras-ocr', folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # BytesIO를 사용하여 이미지 데이터를 메모리에 로드합니다
    image = Image.open(BytesIO(response.content))

    # 이미지를 파일로 저장합니다
    image_path = f'results/result-keras-ocr/{folder_name}/captcha_img_{folder_name}.png'
    image.save(image_path)

    # 저장한 이미지를 다시 불러옵니다
    saved_image = Image.open(image_path)

    # 모델 예측
    pred_texts = process_and_predict(saved_image)
    print(f'OCR 결과 : {pred_texts}')

    # 추출한 텍스트를 파일로 저장합니다
    result_path = f'results/result-keras-ocr/{folder_name}/result_{folder_name}.txt'
    utils.save_to_file(result_path, pred_texts[0])
else:
    print("이미지를 다운로드할 수 없습니다.")
