from PIL import Image
from pylab import *

im = Image.open('lenna.png')

# 转灰度图
imshow(im.convert('L'))
# 缩略图
# im.thumbnail((128, 128))
# imshow(im)

show()