import dicom_parse as dp
import dicomPreprocess as dpp
import mat2numpy as m2n

import matplotlib.pyplot as plt
import numpy as np


img1 = dp.getdicomdir('test_dataset/1')
print(img1.shape)

img2 = m2n.loadimage('test_dataset/1/image.mat')
print(img2.shape)

num_str, mask, name = m2n.parsemask('test_dataset/1/mask.mat')
print("Number of structures : ", num_str)

contour_name = 'GTVp'

for i in range(num_str):
    if name[i] == contour_name:
        num = i

batch_size = 10

"""
print(img1[0:10].shape)
print(mask[num][0:10].shape)
"""


plt.subplot(131)
plt.imshow(img1[10],cmap='gray')
plt.subplot(132)
plt.imshow(img2[10],cmap='gray')


plt.subplot(133)
plt.imshow(mask[num][10],cmap='gray')

plt.show()




"""
resized_dcm = dpp.rotate90(dcmImagesSorted[0])
resized_dcm = dpp.bitresample(resized_dcm)

print(resized_dcm.shape)
plt.imshow(dpp.rotate(resized_dcm,15))
plt.show()
"""