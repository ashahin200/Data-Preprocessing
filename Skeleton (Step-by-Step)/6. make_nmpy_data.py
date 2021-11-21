
# Importing necessary libraries
import os
import glob
import cv2
import pandas as pd
import numpy as np
import sys
from PIL import Image

num_class = 10

data_dir= r''
paths_all_train_data=glob.glob(os.path.join(data_dir,'*.png'))
path_all_train_label= r'   .csv'

print('Length of total image:', len(paths_all_train_data))



##                 Image Pre-process                               

from skimage.transform import pyramid_gaussian
from resizeimage import resizeimage
import imutils
import scipy.misc
import cv2
from keras.utils import to_categorical

def get_key(path):  # it will seperate the filenames from input.csv fle 
    # seperates the key of an image from the filepath     
    key=path.split(sep=os.sep)[-1]
    return key

def get_data(paths_img,path_label=None,resize_dim=None):
# paths_img = paths_all_train_data  
# path_label = path_train_label
    X=[] # initialize empty list for all  image stack
    for i,path in enumerate(paths_img):
        img=cv2.imread(path) # images loaded in color (BGR)
        # print(img.shape)
        X.append(img)
        # display progress
        if i==len(paths_img)-1:
            end='\n'
        else: end='\r'
        print('processed {}/{}'.format(i+1,len(paths_img)),end=end)
    # print(X)
       
    X=np.array(X) # tranform list to numpy array
    if  path_label is None:
        return X
    else:
        df = pd.read_csv(path_label) # read labels
        df=df.set_index('filenames') 
        y_label=[df.loc[get_key(path)]['class_label'] for path in  paths_img] # get the labels corresponding to the images
        y=to_categorical(y_label,num_class) # transfrom integer value to categorical variable
        return X, y
        
###################################################################################################################################

#######                                 load data                   ########

X_train,y_train = get_data(paths_all_train_data,path_all_train_label)

X_train_all= X_train #.astype('float16')  #np.concatenate((X_train_a,X_train_b,X_train_c,X_train_d,X_train_e),axis=0)
y_train_all= y_train  #np.concatenate((y_train_a,y_train_b,y_train_c,y_train_d,y_train_e),axis=0)
print('X_train.shape :', X_train_all.shape)
print('y_train.shape :', y_train_all.shape)

###################################################################################################################################

#######                                 train_val split                    ########

'''    
for Bi-LSTM input are 5D array (batch_size, time_step, img_hight, img_weight, img_channel)
#X_train_all = X_train_all.reshape(X_train_all.shape[0],1, 28, 28, 3).astype('float32')
#X_train_all = X_train_all/255
'''

indices=list(range(len(X_train_all)))
np.random.seed(42)
np.random.shuffle(indices)

ind=int(len(indices)*0.80)
# train data
X_train=X_train_all[indices[:ind]] 
y_train=y_train_all[indices[:ind]]
# validation data
X_val=X_train_all[indices[-(len(indices)-ind):]] 
y_val=y_train_all[indices[-(len(indices)-ind):]]



print('train_split:', X_train.shape) 
print('val_split :', X_val.shape)

np.save('./numpy/X_train.npy', X_train)
np.save('./numpy/y_train.npy', y_train)
np.save('./numpy/X_val.npy', X_val)
np.save('./numpy/y_val.npy', y_val)

print(X_train, y_train, )