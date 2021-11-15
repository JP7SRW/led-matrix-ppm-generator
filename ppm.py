import os
import shutil
from PIL import Image, ImageFont, ImageDraw

def create_ppm(file_name, text, text_r, text_g, text_b, bg_r, bg_g, bg_b):
  font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", 16)
  width, height = font.getsize(text)
  
  img = Image.new("RGB", (width, 16), (bg_r, bg_g, bg_b))
  draw = ImageDraw.Draw(img)
  draw.text((0, 0), text, (text_r, text_g, text_b), font=font)

  img.save("./ppm_files/" + str(file_name) + ".ppm")
  img.save("./png_files/" + str(file_name) + ".png")

def merge_ppm():
  DIR = "./ppm_files/"
  number_of_files = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))

  shutil.copy("./ppm_files/snd_lab.ppm", "./ppm_files/merged.ppm")
  shutil.copy("./png_files/snd_lab.png", "./png_files/merged.png")

  for i in range(number_of_files - 2):
    img1 = Image.open("./ppm_files/" + "merged" + ".ppm")
    img2 = Image.open("./ppm_files/" + str(i) + ".ppm")

    if i == (number_of_files - 3):
      img = Image.new("RGB", (img1.width + 100 + img2.width + 100, img1.height))
      img.paste(img1, (0, 0))
      img.paste(img2 , (100 + img1.width, 0))
    else:  
      img = Image.new("RGB", (img1.width + 100 + img2.width, img1.height))
      img.paste(img1, (0, 0))
      img.paste(img2 , (100 + img1.width, 0))

    img.save("./ppm_files/merged.ppm")
    img.save("./png_files/merged.png")