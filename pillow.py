from PIL import Image
from pylab import *

# im = Image.open('lenna.png')
# 转灰度图
# imshow(im.convert('L'))
# 缩略图
# im.thumbnail((128, 128))
# imshow(im)

im = array(Image.open('lenna.png').convert('L'))

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)

show()