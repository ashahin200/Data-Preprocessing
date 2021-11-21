# Image_augmentation

Computer vision needs lots of images. But in real world this quantity is less and it is always to collect lots of image. In computer vision every algorithm works a number of images. So, in this project we will see that how we get this lots of image easily using programmatically. For this reason, we will use python image processing tools. Keras deep learning framework. 
Before go through we we need which python or deep learning library reads image as a NumPy array. Because for further processing an image every image must be converted to an NumPy array. 
Again, for further processing an image using computer vision algorithm it takes  NumPy array of rank 4 or a tuple 4 such as (batch size, img_height, img_width, channel) . Batch size means how many images we have been used for training/ processing. For this reason, we have need reshape the image size to increase its dimension.
