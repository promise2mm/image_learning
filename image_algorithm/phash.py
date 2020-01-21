import numpy
import cv2


#  pHash算法 快速简单易实现 缺点是无法支持旋转不变性
def p_hash(src):
    hash_len = 32

    #  灰度
    gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #  压缩
    #  resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len))
    #  resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len), interpolation=cv2.INTER_LANCZOS4)
    resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len), interpolation=cv2.INTER_AREA)  # 似乎最准确
    #  resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len), interpolation=cv2.INTER_LINEAR)
    #  resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len), interpolation=cv2.INTER_NEAREST)
    #  resize_gray_img = cv2.resize(gray_img, (hash_len, hash_len), interpolation=cv2.INTER_CUBIC)

    #  图像内的整型转为浮点数便于dct
    h, w = resize_gray_img.shape[:2]  # 获取图像宽高
    vis0 = numpy.zeros((h, w), numpy.float32)  # 初始化
    #  vis0 = numpy.zeros((h, w), numpy.int8)# 初始化
    vis0[:h, :w] = resize_gray_img  # 填充数据

    #  离散余弦变换
    vis1 = cv2.dct(cv2.dct(vis0))
    vis1.resize(hash_len, hash_len)
    img_list = vis1.flatten()
    #  img_list = vis0.flatten()

    #  计算均值
    avg = sum(img_list) * 1. / len(img_list)
    avg_list = []
    for i in img_list:
        if i < avg:
            tmp = '0'
        else:
            tmp = '1'
        avg_list.append(tmp)

    #  计算哈希值
    p_hash_str = ''
    for x in range(0, hash_len * hash_len, 4):
        p_hash_str += '%x' % int(''.join(avg_list[x:x + 4]), 2)
    return p_hash_str


def ham_dist(x, y):
    assert len(x) == len(y)
    return sum([ch1 != ch2 for ch1, ch2 in zip(x, y)])


if __name__ == '__main__':
    img1 = 'resources/images/IMG_5571.JPG'
    img2 = 'resources/images/IMG_6696.JPG'

    img3 = 'resources/ace2.png'
    img4 = 'resources/ace3.png'

    #   读取图像
    img_src = cv2.imread(img3)
    img_diff = cv2.imread(img4)

    hash_src = p_hash(img_src)
    hash_diff = p_hash(img_diff)

    print('src:\t%s' % hash_src)
    print('diff:\t%s' % hash_diff)
    print('ham-src-diff:\t%s' % ham_dist(hash_src, hash_diff))  # 完全不同的图像  汉明距大于10
