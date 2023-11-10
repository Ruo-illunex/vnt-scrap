import requests
from io import BytesIO

from PIL import Image
from model.model import process_and_predict

from src import settings


# 이미지 URL
url = settings.captcha_img_url

# requests를 사용하여 이미지를 가져옵니다
response = requests.get(url)

# 이미지가 정상적으로 다운로드 되었는지 확인
if response.status_code == 200:
    # BytesIO를 사용하여 이미지 데이터를 메모리에 로드합니다
    image = Image.open(BytesIO(response.content))

    # 이미지를 파일로 저장합니다
    image_path = 'captcha_img/captcha.png'
    image.save(image_path)

    # 저장한 이미지를 다시 불러옵니다
    saved_image = Image.open(image_path)

    # 모델 예측
    pred_texts = process_and_predict(saved_image)
    print(f'OCR 결과 : {pred_texts}')

else:
    print("이미지를 다운로드할 수 없습니다.")
