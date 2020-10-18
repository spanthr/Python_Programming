# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:22:04 2020

@author: shaur
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
# Read the image. 

img = cv2.imread('testimage.jpg')
cv2.imshow('Orignal',img)
cv2.waitKey(0)
# img.imshow('image',img)
# Apply bilateral filter
d=15
sigmaSpace=75
sigmaColor =75

  
bilateral = cv2.bilateralFilter(img, d, sigmaSpace, sigmaColor) 
# Save the output. 
cv2.imwrite('bilateral.jpg', bilateral)
cv2.imshow('Filtered',bilateral)
cv2.waitKey(0)

# d: Diameter of each pixel neighborhood.
# sigmaColor: Value of \sigma in the color space. 
# The greater the value, the colors farther to each other will start to get mixed.
# sigmaColor: Value of \sigma in the coordinate space. 
# The greater its value, the more further pixels will mix together,
 # given that their colors lie within the sigmaColor range.
plt.axis("off")
plt.title("Orignal Image")
i1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(i1)

plt.show()
plt.axis("off")
plt.title("Filtered Image")
i2=cv2.cvtColor(bilateral,cv2.COLOR_BGR2RGB)
plt.imshow(i2)
