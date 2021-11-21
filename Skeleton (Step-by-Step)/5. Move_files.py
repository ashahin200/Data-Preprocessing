import shutil, os


input_path  = r''
output_path  = r''

files = os.listdir(input_path)

for file_index, file in enumerate(files):
    file_path = os.path.join(input_path, file)
    subfiles = os.listdir(file_path)

    for index, subfile in enumerate(subfiles):
        image_path = os.path.join(file_path, subfile)
        # print(image_path)
        shutil.copy(image_path, output_path)
        print("preprocessing(move): folder number ",file_index+1," and within this folder image number: ", index+1)

