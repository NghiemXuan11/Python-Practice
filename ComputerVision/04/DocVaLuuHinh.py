import os
from PIL import Image
from imgtools import *
print("Hello world")
# Thu muc chua hinh anh
dir = 'D:/Python-Practice/ComputerVision/03/img'

# Duong dan den hinh anh
image_path = dir + "/Anh_1.jpg"
print(image_path)

# Su dung ham Image.open() doc anh
img01 = Image.open(image_path)

# Hien thi hinh anh
img01.show()

# In 1 so thong tin
# In dinh dang anh
print("Dinh dang anh: " + img01.format)

# In ra size
print("Kich thuoc hinh anh: ", img01.size)

# Luu anh va chuyen doi
new_img_01_path = dir + "/new_01.JPG"
new_img_png_01_path = dir + "/new_01.PNG"
img01.save(new_img_01_path)
img01.save(new_img_png_01_path)


# Đọc ảnh từ function imagetools.
img01 = load_image(image_path)
img01.show()

# Dong tap tin
img01.close()




