import os
import cv2
from PIL import Image
from resizeimage import resizeimage
import os

path = r"  "
files = os.listdir(path)


desired_size = 50

total_image =  0
for file_index, file in enumerate(files):
    file_path = os.path.join(path, str(file_index))
    subfiles = os.listdir(file_path)


    img_num = 0
    for index, subfile in enumerate(subfiles):
        dir_path = os.path.join(path, str(file_index))
        image_path = os.path.join(dir_path, subfile)
        img = Image.open(image_path)
        img = resizeimage.resize_contain(img, [desired_size, desired_size])
        img.save(image_path , img.format)
        print("preprocessing(resize): folder number ",file_index+1," and within this folder image number: ", index+1)
        img_num = img_num +1


    print(img_num)
    print("--------------------------------------------------")
    total_image = total_image + img_num


print("After preprocessing(rename): total image number: ", total_image)
