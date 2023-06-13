# Sculp Data : Valid Load

import os

from PIL import Image

valid_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image/Validation/'
valid_resize_dir_ = 'C:/Users/User/MLproject/ML-Final_Project/Scalp_Image_Resize/Valid_Resize/'

valid_files = os.listdir(valid_dir_)

for (valid_root, valid_dircetories, valid_files) in os.walk(valid_dir_):
    for valid_file in valid_files:
        if '.jpg' in valid_file:
            if valid_root == valid_dir_ + '[원천]모낭사이홍반_0.양호':
                if not os.path.exists(valid_resize_dir_ + "10"):
                    os.mkdir(valid_resize_dir_ + "10")
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/10/{valid_file}")
                else:
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/10/{valid_file}")
            
            elif valid_root == valid_dir_ + '[원천]모낭사이홍반_1.경증':
                if not os.path.exists(valid_resize_dir_ + "11"):
                    os.mkdir(valid_resize_dir_ + "11")
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/11/{valid_file}")
                else:
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/11/{valid_file}")
            
            elif valid_root == valid_dir_ + '[원천]모낭사이홍반_2.중등도':
                if not os.path.exists(valid_resize_dir_ + "12"):
                    os.mkdir(valid_resize_dir_ + "12")
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/12/{valid_file}")
                else:
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/12/{valid_file}")
            
            elif valid_root == valid_dir_ + '[원천]모낭사이홍반_3.중증':
                if not os.path.exists(valid_resize_dir_ + "13"):
                    os.mkdir(valid_resize_dir_ + "13")
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/13/{valid_file}")
                else:
                    img = Image.open(valid_root + "/" + valid_file)
                    print(os.path.join(valid_root, valid_file))
                    img_resize = img.resize((320, 240))
                    img_resize.save(f"{valid_resize_dir_}/13/{valid_file}")
            
          
            else:
                print(valid_root)
                break

        else:
            break