import numpy as np
from huggingface_hub import from_pretrained_keras
import tensorflow as tf
import keras
from keras import layers


# 이미지 크기
img_height = 50
img_width = 200
max_length = 6
characters = "0123456789"

# 문자를 숫자로 변환하는 레이어를 만듭니다
char_to_num = layers.StringLookup(
    vocabulary=list(characters), mask_token=None
)

# 한 번에 하나의 문자를 예측하는 모델을 만듭니다
num_to_char = layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), mask_token=None, invert=True
)


def encode_single_sample(img):
    # 이미지를 grayscale로 변환
    img = img.convert('L')
    # 이미지를 NumPy 배열로 변환
    img = np.array(img)
    # 채널 차원 추가 (높이, 너비) -> (높이, 너비, 1)
    img = np.expand_dims(img, axis=-1)
    # 이미지를 Tensor로 변환하고 정규화
    img = tf.convert_to_tensor(img, dtype=tf.float32) / 255.0
    # 이미지 크기 조정
    img = tf.image.resize(img, [img_height, img_width])
    # 이미지 전치
    img = tf.transpose(img, perm=[1, 0, 2])
    # 이미지 차원 확장 (batch 차원 추가)
    img = tf.expand_dims(img, axis=0)
    return img


# 모델의 입력과 출력을 정의합니다
def decode_batch_predictions(pred):
    input_len = np.ones(pred.shape[0]) * pred.shape[1]
    # CTC 디코딩
    results = keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][
        :, :max_length
    ]
    # 결과를 정수에서 문자열로 변환
    output_text = []
    for res in results:
        res = tf.strings.reduce_join(num_to_char(res)).numpy().decode("utf-8")
        output_text.append(res)
    return output_text


# 이미지를 처리하고 예측을 수행하는 방법
def process_and_predict(image):
    # 이미지 전처리
    processed_image = encode_single_sample(image)

    # 모델 예측
    preds = prediction_model.predict(processed_image)

    # 결과 디코딩
    pred_texts = decode_batch_predictions(preds)

    return pred_texts


# 모델의 입력과 출력을 정의합니다
model = from_pretrained_keras("keras-io/ocr-for-captcha")

prediction_model = keras.models.Model(
    inputs=model.get_layer(name="image").input,
    outputs=model.get_layer(name="dense2").output
)
