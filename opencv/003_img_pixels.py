import cv2 as cv

src = cv.imread('../resources/ace3.png')
cv.imshow('input', src)

h, w, ch = src.shape

print('h, w, ch:', h, w, ch)

# 图像颜色反转
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        src[row, col] = [255 - b, 255 - g, 255 - r]
cv.imshow('output', src)
cv.waitKey(0)
cv.destroyAllWindows()
