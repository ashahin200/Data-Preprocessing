import os
path =  r" "
files = os.listdir(path)

# file_name = [
#                 [0, 'zero'], [1, 'one'], [2, 'two'], [3, 'three'], [4, 'four'],
#                 [5, 'five'], [6, 'six'], [7, 'seven'], [8, 'eight'], [9, 'nine'], [10, 'ten'], [11, 'eleven'], [12, 'twelve'], [13, 'thirteen'], [14, 'fourteen'],
# ]
file_name = [

           [0, 'zero'], [1, 'one'], [2, 'two'], [3, 'three'], [4, 'four'],
              [5, 'five'], [6, 'six'], [7, 'seven'], [8, 'eight'], [9, 'nine']
]


print(len(file_name))

total_image = 0
for file_index, file in enumerate(files):
    file_path = os.path.join(path, str(file_index))
    subfiles = os.listdir(file_path)


    img_num = 0
    for index, subfile in enumerate(subfiles):

        dir_path = os.path.join(path, str(file_index))
        image_path = os.path.join(dir_path, subfile)
        os.rename(image_path, os.path.join(dir_path, str(file_name[file_index][0])+file_name[file_index][1]+'.'+str(index)+'.png' ))

        # file = (image_path, os.path.join(dir_path, str(file_name[file_index][0])+file_name[file_index][1]+'.'+str(index)+'.png' ))
        # print(subfile)

        img_num = img_num +1
        print("preprocessing(rename): folder number ",file_index+1," and within this folder image number: ", index+1)

    print(img_num)
    print("--------------------------------------------------")
    total_image = total_image + img_num


print("After preprocessing(rename): total image number: ", total_image)






