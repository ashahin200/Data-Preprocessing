import os
import pandas as pd
import glob

root_path = r'  '
 
num_class = 10

# file_names = [  'zero','one', 'two', 'three', 'four', 'five', 'six',
#                'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
#                'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
#                'ninteen', 'twenty', 'twenty_one', 'twenty_two', 'twenty_three', 'twenty_four',
#                'twenty_five', 'twenty_six', 'twenty_seven', 'twenty_eight', 'twenty_nine', 'thirty',
#                'thirty_one', 'thirty_two', 'thirty_three', 'thirty_four', 'thirty_five',
#             ]

file_names = [
                   'zero','one', 'two', 'three', 'four', 'five', 'six',
                'seven', 'eight', 'nine'
]

for i in range(num_class):
    path = os.path.join(root_path, str(i))
    files = os.listdir(path)
    total_file = len(files)
    print(total_file)

    df = pd.DataFrame()
    df['filenames'] = [str(i)+file_names[i]+"."+str(x)+".png" for x in range(total_file)]
    df['class_label'] = i

    save_path = r' '
    df.to_csv(os.path.join(save_path, str(i))+".csv")
    print(save_path)


# get data file names
path = r   '
filenames = [os.path.join(path, str(i))+".csv" for i in range(num_class)]  #C:\Users\Sphinx\Desktop\Python-Toolkit\csv\0.csv
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)
big_frame.to_csv("./input.csv")
print(filenames)
