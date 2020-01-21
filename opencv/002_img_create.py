import cv2 as cv
import numpy as np

src = cv.imread('../resources/ace3.png')
cv.imshow('ace3', src)

# 克隆图像
m1 = np.copy(src)

# 赋值 - 将某个区域内的值设置为255
m2 = src
src[100:200, 200:300, :] = 255
cv.imshow('m2', m2)

# 置零
m3 = np.zeros(src.shape, src.dtype)
cv.imshow('m3', m3)

m4 = np.zeros([128, 128], np.uint8)
# 全部设置为127
# m4[:, :] = 127
cv.imshow('m4', m4)

m5 = np.ones(shape=[300, 300, 3], dtype=np.uint8)
cv.imshow("m5", m5)

cv.waitKey(0)
cv.destroyAllWindows()
