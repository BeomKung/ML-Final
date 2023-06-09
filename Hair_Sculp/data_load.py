# Sculp Data Load

import os
import numpy as np

from PIL import Image

train_dir_ = '../../Final_Project_Data/Scalp_Image/Training'
valid_dir_ = '../../Final_Project_Data/Scalp_Image/Validation'

train_files = os.listdir(train_dir_)
valid_files = os.listdir(valid_dir_)

train_img_list = [img for img in train_files if img.endswith('.jpg')]
valid_img_list = [img for img in valid_files if img.endswith('.jpg')]

print(len(train_img_list))
print(len(valid_img_list))