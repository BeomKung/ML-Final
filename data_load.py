# Data Load

import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# 데이터 불러오기
dir_ = '../Final_Project_Data/Image_All/'

all_files = os.listdir(dir_)
image_list = [img for img in all_files if img.endswith('.jpg')]

# 넘파이 배열 변환
image_list_numpy = []

for i in image_list:
    img = Image.open(dir_ + i)
    img_resize = img.resize((256, 256))
    img_convert = img_resize.convert("L")
    image_array = np.array(img_convert)
    image_list_numpy.append(image_array)

# 리스트 전체 변환
image_numpy = np.array(image_list_numpy)
print(image_numpy.shape)    # (1142(개 데이터), 256(가로 픽셀), 256(세로 픽셀), 3(RGB))

image_2D = image_numpy.reshape(-1, 256 * 256)
print(image_2D.shape)       # (3426(개 데이터), 65536(256 * 256))

plt.imshow(image_numpy[1], cmap='gray')
plt.show()