import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\samue\Documents\Resources\alce.png", cv2.IMREAD_COLOR)
img_corr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_slice_1 = img_corr[0:143, 0:194]
img_slice_2 = img_corr[0:143, 194:388, 1]
img_slice_3 = img_corr[143:286, 194:388, 0]
img_slice_4 = img_corr[143:286, 0:194, 2]

img_modified = np.zeros(np.shape(img_corr), dtype=np.uint8)

img_modified[0:143, 0:194, 0] = img_slice_1[:,:,2]
img_modified[0:143, 0:194, 1] = img_slice_1[:,:,1]
img_modified[0:143, 0:194, 2] = img_slice_1[:,:,0]

img_modified[0:143, 194:388, 0] = img_slice_2[:,:]
img_modified[0:143, 194:388, 1] = 0
img_modified[0:143, 194:388, 2] = 0

img_modified[143:286, 194:388, 0] = 0
img_modified[143:286, 194:388, 1] = 0
img_modified[143:286, 194:388, 2] = img_slice_3[:,:]

img_modified[143:286, 0:194, 0] = 0
img_modified[143:286, 0:194, 1] = img_slice_4[:,:]
img_modified[143:286, 0:194, 2] = 0

img_modified = cv2.cvtColor(img_modified,cv2.COLOR_BGR2RGB)

plt.imshow(img_modified, cmap = 'gray')
plt.show()
