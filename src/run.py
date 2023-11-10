import re
import requests
from io import BytesIO

from PIL import Image
import pytesseract

# 이미지 URL
url = 'https://www.smes.go.kr/venturein/pbntc/captchaImg.do'

# requests를 사용하여 이미지를 가져옵니다
response = requests.get(url)

# 이미지가 정상적으로 다운로드 되었는지 확인
if response.status_code == 200:
    # BytesIO를 사용하여 이미지 데이터를 메모리에 로드합니다
    image = Image.open(BytesIO(response.content))

    # 이미지를 파일로 저장합니다
    image_path = '../captcha_img/captcha.png'
    image.save(image_path)

    # 저장한 이미지를 다시 불러옵니다
    saved_image = Image.open(image_path)

    config = ('--oem 3 --psm 6')
    # pytesseract를 사용하여 저장된 이미지에서 텍스트를 추출합니다
    text = pytesseract.image_to_string(saved_image, config=config)
    print(f'OCR 결과 : {text}')
    print(f'Length: {len(text)}')

    numbers = re.findall(r'\d+', text)
    print(numbers)
else:
    print("이미지를 다운로드할 수 없습니다.")
