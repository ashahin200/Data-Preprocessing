# #Multiclass. Read dirctly from the folder structure using flow_from_directory and save it a new folder
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


i = 0
for batch in datagen.flow_from_directory(directory='images/test_images/', 
                                         batch_size=16,  
                                         target_size=(56, 56),
                                         color_mode="rgb",
                                         save_to_dir='augmented', 
                                         save_prefix='aug', 
                                         save_format='png'):
    i += 1
    if i > 10:
        break 