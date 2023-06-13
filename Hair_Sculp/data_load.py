# Sculp Data Load

import os
import numpy as np

from PIL import Image

train_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image/Training/'
valid_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image/Validation/'
train_resize_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Train_Resize/'
valid_resize_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Valid_Resize/'

train_files = os.listdir(train_dir_)
valid_files = os.listdir(valid_dir_)

train_image_list_numpy = []
valid_image_list_numpy = []

for (train_root, train_directories, train_files) in os.walk(train_dir_):
    for train_file in train_files:
        if '.jpg' in train_file:
            if train_root == train_dir_ +'[원천]모낭사이홍반_0.양호':
                if not os.path.exists(train_resize_dir_ + "10"):
                    os.mkdir(train_resize_dir_ + "10")
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/10/{train_file}")
                else:
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/10/{train_file}")
            elif train_root == train_dir_ +'[원천]모낭사이홍반_1.경증':
                if not os.path.exists(train_resize_dir_ + "11"):
                    os.mkdir(train_resize_dir_ + "11")
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/11/{train_file}")
                else:
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/11/{train_file}")
            elif train_root == train_dir_ +'[원천]모낭사이홍반_2.중등도':
                if not os.path.exists(train_resize_dir_ + "12"):
                    os.mkdir(train_resize_dir_ + "12")
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/12/{train_file}")
                else:
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/12/{train_file}")
            elif train_root == train_dir_ +'[원천]모낭사이홍반_3.중증':
                if not os.path.exists(train_resize_dir_ + "13"):
                    os.mkdir(train_resize_dir_ + "13")
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/13/{train_file}")
                else:
                    img = Image.open(train_root + "/" + train_file)
                    print(os.path.join(train_root, train_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{train_resize_dir_}/13/{train_file}")
            else:
                break
        else:
            break

            # print(train_root)
            # img = Image.open(train_root + "/" + train_file)
            # print(os.path.join(train_root, train_file))
            # img_resize = img.resize((320, 240))
            # train_image_list_numpy.append(img_resize)


# for (valid_root, valid_directories, valid_files) in os.walk(valid_dir_):
#     for valid_file in valid_files:
#         if '.jpg' in valid_file:
#             img = Image.open(valid_root + "/" + valid_file)
#             print(os.path.join(valid_root, valid_file))
#             img_resize = img.resize((320, 240))
#             valid_image_list_numpy.append(img_resize)



# print(len(train_image_list_numpy))
# print(len(valid_image_list_numpy))