from keras.preprocessing.image import ImageDataGenerator
from skimage import io

datagen = ImageDataGenerator(
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='reflect')    #Also try nearest, constant, reflect, wrap

# Loading a sample image Can use any library to read images but they need to be in an array form
x = io.imread('---------------')  #Array with shape (img_height, img_width, channel) 

# Need to Reshape image because Input data to datagen.flow must be Numpy array of rank 4 or a tuple.
x = x.reshape((1, ) + x.shape)  #Array with shape (batch size, img_height, img_width, channel) 

#  that will make 10 aumented image  
i = 0
for batch in datagen.flow(x, 
                          save_to_dir='augmented', 
                          save_prefix='aug', 
                          save_format='png'):
    i += 1
    if i > 10:
        break 