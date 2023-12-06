"""Images lesson, Menoko OG, 11-2023"""
from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
img.thumbnail((400, 400)) # this method versus resize keeps the aspect of image instead of squishing it
img.save("thumbastro.jpg")

