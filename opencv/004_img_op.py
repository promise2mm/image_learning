import cv2 as cv
import numpy as np

# 图片的加减乘除操作

src1 = cv.imread('../resources/ace2.png')
src2 = cv.imread('../resources/ace3.png')

cv.imshow('src1', src1)
cv.imshow('src2', src2)

add_result = np.zeros(src1.shape, src1.dtype)
cv.add(src1, src2, add_result)
cv.imshow('add', add_result)

sub_result = np.zeros(src1.shape, src1.dtype)
cv.subtract(src2, src1, sub_result)
cv.imshow('subtract', sub_result)

multi_result = np.zeros(src1.shape, src1.dtype)
cv.multiply(src1, src2, multi_result)
cv.imshow('multi', multi_result)

divide_result = np.zeros(src1.shape, src1.dtype)
cv.add(src1, src2, divide_result)
cv.imshow('divide', divide_result)

cv.waitKey(0)
cv.destroyAllWindows()
