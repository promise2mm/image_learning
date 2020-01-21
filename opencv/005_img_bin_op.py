import cv2 as cv
import numpy as np

# 图片的位操作

# blue - 0
# green - 1
# red - 2

src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 1] = 255
src1[100:200, 100:200, 2] = 255

# src1[100:200, 200:300, 1] = 255
# src1[100:200, 200:300, 1] = 255
#
# src1[200:300, 100:200, 0] = 255
# src1[200:300, 100:200, 0] = 255
#
# src1[200:300, 200:300, 2] = 255
# src1[200:300, 200:300, 2] = 255
cv.imshow('src1', src1)

# create image two
src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[150:250, 150:250, 2] = 255
cv.imshow("src2", src2)

dst1 = cv.bitwise_and(src1, src2)
cv.imshow('and', dst1)

dst2 = cv.bitwise_xor(src1, src2)
cv.imshow('xor', dst2)

dst3 = cv.bitwise_or(dst1, dst2)
cv.imshow('or', dst3)

src = cv.imread('../resources/ace3.png')
cv.imshow('src', src)
dst = cv.bitwise_not(src)
cv.imshow('not', dst)

cv.waitKey(0)
cv.destroyAllWindows()
