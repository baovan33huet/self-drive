from PIL import Image

# Mở hình ảnh
image_path = "track.png"
image = Image.open(image_path)

# Thay đổi kích thước hình ảnh
new_size = (1000, 600)  # Hoặc kích thước bạn muốn
resized_image = image.resize(new_size, Image.LANCZOS)

# Lưu hình ảnh đã thay đổi kích thước
resized_image.save("resize_track.png")
