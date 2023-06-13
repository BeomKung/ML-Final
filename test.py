import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import keras
import numpy as np

# 모델 구성
model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu',padding='same', input_shape=(80, 60, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu',padding='same'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
# model.add(Dense(50, activation='relu'))
model.add(Dense(6, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 이미지 데이터의 경로
train_data_dir = 'C:/Users/User/MLproject/ML-data/Scalp_Image_Resize_1/Train_Resize/'
valid_data_dir = 'C:/Users/User/MLproject/ML-data/Scalp_Image_Resize_1/Valid_Resize/'

# 이미지 데이터를 전처리하고 증강하기 위한 옵션 설정
train_datagen = ImageDataGenerator(
    rescale=1./255,  # 이미지 스케일 조정 (0-255 범위를 0-1 범위로 조정)
    # rotation_range = 15,
    # width_shift_range=0.1,
    # height_shift_range=0.1,
    # shear_range=0.5,
    # zoom_range=[0.8,2.0],
    # horizontal_flip=True,
    # fill_mode='nearest'
    # shear_range=0.2,  # 이미지 전단 변환 적용
    # zoom_range=0.2,  # 이미지 확대/축소 변환 적용
    # horizontal_flip=True  # 이미지 수평 반전 적용
)

valid_datagen = ImageDataGenerator(rescale=1./255)

# 이미지 데이터를 배치 단위로 로드하고 전처리 수행
train_generator = train_datagen.flow_from_directory(
    train_data_dir,  # 훈련 데이터 폴더 경로
    target_size=(80, 60),  # 이미지 크기 설정
    batch_size=16,  # 배치 크기 설정
    class_mode='categorical'  # 다중 클래스 분류 문제인 경우 'categorical' 설정
)

valid_generator = valid_datagen.flow_from_directory(
    valid_data_dir,  # 검증 데이터 폴더 경로
    target_size=(80, 60),
    batch_size=16,
    class_mode='categorical'
)

steps_per_epoch = len(train_generator)
validation_steps = len(valid_generator)

# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5')

# early_stopping_cb = keras.callbacks.EarlyStopping(patience=5,
#             restore_best_weights=True)
# CNN 모델 학습 및 평가
model.fit(
    train_generator,
    epochs=20,  # 학습 에포크 수 설정
    validation_data=valid_generator,
    steps_per_epoch= steps_per_epoch,
    validation_steps = validation_steps,
    # callbacks=[checkpoint_cb, early_stopping_cb]
)

model.evaluate(valid_generator)
# # 예측할 이미지 파일 경로
# test_image_path = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Valid_Resize/30/6995_A2LEBJJDE00104R_1606040549648_5_RH.jpg'

# # 이미지 로드 및 전처리
# img = image.load_img(test_image_path, target_size=(320, 240))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = x / 255.0  # 이미지 스케일 조정

# # 예측
# predictions = model.predict(x)

# # 예측 결과 출력
# class_indices = train_generator.class_indices
# predicted_class = list(class_indices.keys())[np.argmax(predictions)]
# print('Predicted class:', predicted_class)

