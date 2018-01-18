import numpy as np
import skimage.transform as sktf

# Reduce dicom size from 512 x 512 to 227 x 227
def resize(dcmimage, resize_shape=(227,227)):
    if dcmimage.shape != (512,512):
        print("The size of DICOM is not 512 X 512. Please check again!")
        return

    return sktf.resize(dcmimage, resize_shape, mode="constant")


### bit resampling ###
def bitresample(dcmimage, bit=8):
    print(dcmimage.min(), dcmimage.max())
    return dcmimage



### Functions for Data Augmentation ###
### Geometric rotation & flip ###
# Rotate dicom by given degree in clockwise
def rotate(dcmimage, angle):
    return sktf.rotate(dcmimage,angle=angle)

# Rotate dicom by 90 degree in clockwise
def rotate90(dcmimage):
    return sktf.rotate(dcmimage,angle=90)

# Rotate dicom by 180 degree in clockwise
def rotate180(dcmimage):
    return sktf.rotate(dcmimage,angle=180)

# Rotate dicom by 270 degree in clockwise
def rotate270(dcmimage):
    return sktf.rotate(dcmimage,angle=270)

# Flip left to right
def fliplr(dcmimage):
    return np.fliplr(dcmimage)

# Flip upside down
def flipud(dcmimage):
    return np.flipud(dcmimage)



