from keras.preprocessing.image import ImageDataGenerator
from skimage import io

datagen = ImageDataGenerator(
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='reflect')  

import numpy as np
from skimage import io
import os
from PIL import Image

image_directory = './-------------'
SIZE = 128
dataset = []

my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((SIZE,SIZE))
        dataset.append(np.array(image))    

x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=16,  
                          save_to_dir='augmented', 
                          save_prefix='aug', 
                          save_format='png'):
    i += 1
    if i > 10:
        break