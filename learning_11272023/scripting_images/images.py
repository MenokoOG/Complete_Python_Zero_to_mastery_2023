"""Python working with images lesson, Menoko OG, 11-2023"""
from PIL import Image, ImageFilter

img = Image.open("./pokadex/pikachu.jpg")
filtered_img = img.convert("L")
filtered_img_blur = img.filter(ImageFilter.BLUR)
filtered_img_blur.save("pikablur.png", "png")
filtered_img_sharp = img.filter(ImageFilter.SHARPEN)
filtered_img_sharp.save("pikasharp.png", "png")
box = (100, 100, 400, 400) # crop method
region = filtered_img.crop(box)
region.save("pikacrop.png", "png")
filtered_img.save("pikagrey.png", "png")
crooked = img.rotate(90)
crooked.save("pikacrooked.png", "png")
resize = filtered_img.resize((300, 300))
resize.save("pikaresize.png", "png")

# filtered_img.show() # opens image application to show image.
# pikacrooked.show()

# print(img.format)
# print(img.size)
# print(img.mode)