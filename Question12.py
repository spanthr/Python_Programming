import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
img2 = img.copy()
template = cv2.imread('messi_face.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    temp_match=cv2.matchTemplate(img, template, method)
    # Finds the global minimum and maximum in an array.
    min_val,max_val, min_position, max_position=cv2.minMaxLoc(temp_match)
    if method in [cv2.TM_SQDIFF_NORMED] or  method in [cv2.TM_SQDIFF]:
        dimension1=min_position
    else:
        dimension1=max_position
    dimension2=(dimension1[0]+w,dimension1[1]+h)
    
    cv2.rectangle(img,dimension1,dimension2,255,2)
    
    plt.subplot(121),plt.imshow(temp_match,cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

