# Sculp Data Load

import os

from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

valid_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize_1/valid_Resize/'
valid_resize_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize_1/valid_Resize/'
valid_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize_1/Valid_Resize/'
valid_resize_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize_1/Valid_Resize/'

valid_files = os.listdir(valid_dir_)
valid_files = os.listdir(valid_dir_)

for (valid_root, valid_directories, valid_files) in os.walk(valid_dir_):
    for valid_file in valid_files:
         if '.jpg' in valid_file:
            print(valid_file)
            if valid_root == valid_dir_ + "63":
                img = Image.open(valid_root + "/" + valid_file)
                print(os.path.join(valid_root, valid_file))
                # img_top_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
                img_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
                img_horizontal.save(f"{valid_resize_dir_}/63-1/HORIZON_{valid_file}")
            else:
                print("break")