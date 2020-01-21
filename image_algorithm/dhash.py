from DHash import DHash as DHash
from PIL import Image as Image

resize_width = 9
resize_height = 8

img1 = Image.open('resources/images/IMG_5571.JPG')
hash_value1 = DHash.calculate_hash(img1)

img2 = Image.open('resources/ace3.png')
hash_value2 = DHash.calculate_hash(img2)

print(hash_value1, hash_value2)

distance = DHash.hamming_distance(img1, img2)

if distance < 10:
    print('same image: ' + str(distance))
else:
    print('different image ! ' + str(distance))
