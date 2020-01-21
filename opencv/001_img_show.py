import cv2 as cv

img = cv.imread('../image_algorithm/resources/ace3.png')
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
resize_img = cv.resize(img, (200, 200))
gray_img = cv.cvtColor(resize_img, cv.COLOR_BGR2GRAY)
cv.imshow('input', gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
