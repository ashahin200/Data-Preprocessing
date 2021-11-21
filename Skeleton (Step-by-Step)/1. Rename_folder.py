import os
path = r'  '
files = os.listdir(path)


total_folder = 0
for file_index, file in enumerate(files):
    file_path = os.path.join(path, file)
    os.rename(file_path, os.path.join(path, str(file_index)))
    total_folder = total_folder + 1

print("After preprocessing(rename): Total Folder: ", total_folder)
