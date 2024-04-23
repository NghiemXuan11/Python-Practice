import os
from PIL import Image


def load_image(image_path):
    """
        Đọc ảnh từ đường dẫn cho trước và trả về đối tượng ảnh
        Args: image_path
        Returns: đối tượng hình ảnh
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Lỗi khi đọc hình ảnh từ: ", image_path, " ", e)
        return None
