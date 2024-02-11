import cv2
import numpy as np

"""
Image can be filtered using low pas filter(LPF) for noise removal and high pass fileter(HPF) for edge 
detection

we will exploreLPF
"""
img = cv2.imread('noisy2.jpg')


"""
FILTERING
1) 2D filtering/ Homogeneous filtering

    - here take a odd no. square [(3,3), (5,5), (7,7)] and divide by product of length*width [9,25,49]
    - how it works is place filter above pixel take sum and average, replace the middle pixel with the avg
"""
kernel = np.ones((3,3), np.float32)/9
homo_fil = cv2.filter2D(img, -1, kernel)

"""
BLURING

It will remove noise by removing high frequency value (noise, edges), so edges also removed

Different approaches for bluring using kernel
1) Average bluring - same as 2D filter using normalized box filter
"""
blur = cv2.blur(img,(3,3))

"""
2) Gaussian bluring
    - repalce box filter with guassian filter, has higher value in middl, should be odd
"""

gau = cv2.GaussianBlur(img, (3,3),0)

"""
3) Median bluring
    - instead of taking average it takes median of pixel and replace the middle, best for removing noise 
    and pepper, since median no new pixcel is created
"""

med = cv2.medianBlur(img,3)


"""
4) Bilateral filtering

    - this preserve the edge, while other donts, achive so by using two guassian filter,
        one for removing noise, other compare intensity and check if edge present, edge will have very large
        intensity variation
"""
bi_fil = cv2.bilateralFilter(img, 5,75,75)

import matplotlib.pyplot as plt

images = [img, homo_fil, blur, gau, med, bi_fil]
titles = ['ori', '2 D', 'average blur', 'guassian', 'median', 'bilateral']

for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# cv2.imshow("ori",img)
# cv2.imshow("2D fileter", homo_fil)
# cv2.imshow("blur", blur)
# cv2.imshow("gaussian", gau)
# cv2.imshow("median", med)
# cv2.imshow('bi', bi_fil)
# cv2.waitKey()
# cv2.destroyAllWindows()