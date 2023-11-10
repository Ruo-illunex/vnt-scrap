vnt-scrap
# 벤처기업 공시 데이터 스크래핑을 위한 캡챠 해결 전략

- **목적**: 본 업무는 벤처기업 공시 정보를 효과적으로 수집하기 위한 스크래핑 과정에서 발생하는 캡챠(CAPTCHA) 인증 문제를 해결하기 위함입니다.



- **배경**: 벤처기업 공시 정보는 투자 결정 및 시장 분석에 중요한 데이터를 제공합니다. 그러나, 이 정보를 수집하는 과정에서 자동화된 스크래핑을 방지하기 위한 캡챠 시스템에 자주 부딪힙니다.



- **주요 과제**:
  - 캡챠 인식과 해결을 위한 자동화된 솔루션 개발
  - 스크래핑 프로세스의 효율성 및 정확성 향상
  - 법적 및 윤리적 지침 준수


- **실행 계획**:
  - 최신 OCR(Optical Character Recognition) 기술과 AI 기반 캡챠 해결 알고리즘 조사 및 적용
  - 스크래핑 빈도 조절 및 대상 사이트의 요구 사항에 맞는 접근 방법 마련
  - 데이터 수집 및 처리에 대한 법적 조언 구하기


- **예상 결과**: 이 프로젝트는 벤처기업 공시 정보의 신속하고 정확한 수집을 가능하게 하여, 데이터 기반 의사결정을 위한 타이밍과 정확성을 개선할 것입니다.

# 프로젝트 구조
```
.
├── README.md
├── model
│   ├── __init__.py
│   │   ├── __init__.cpython-310.pyc
│   │   └── model.cpython-310.pyc
│   └── model.py
├── ocr_model.py
├── poetry.lock
├── pyproject.toml
├── results
│   ├── result-keras-ocr
│   └── result-pytesseract
├── run.py
└── src
    ├── __init__.py
    │   ├── __init__.cpython-310.pyc
    │   ├── settings.cpython-310.pyc
    │   └── utils.cpython-310.pyc
    ├── gpu-check.py
    ├── settings.py
    └── utils.py
```

- run.py: tesseract 모델 실행 스크립트입니다.
- ocr_model.py: keras-ocr 모델과 관련된 작업을 수행하는 스크립트입니다.
- model 디렉토리:
  - model.py: 프로젝트의 주요 모델 논리가 포함된 스크립트입니다.
- results 디렉토리:
  - result-keras-ocr 및 result-pytesseract: 이들 하위 디렉토리는 OCR 작업의 결과를 저장합니다. 각 디렉토리는 날짜 및 시간별로 구분되며, 각각의 디렉토리 안에는 OCR 처리된 이미지(captcha_img)와 결과 텍스트(result.txt) 파일이 포함되어 있습니다.
- src 디렉토리:
  - gpu-check.py: GPU 상태를 체크하는 유틸리티 스크립트입니다.
  - settings.py: 프로젝트 설정 관련 스크립트입니다.
  - utils.py: 일반적인 유틸리티 함수를 포함하는 스크립트입니다.
- poetry.lock 및 pyproject.toml: 의존성 관리 및 프로젝트 설정을 위한 파일입니다.
