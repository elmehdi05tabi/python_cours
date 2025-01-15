# ---------------------------------------------------------
# --Practical => Image Manipulation with Pillow --
# ---------------------------------------------------------
from PIL import Image 
# ovrir la photo 
myimg = Image.open(r"C:\Users\tabi\Desktop\man.jpg")
# sho image 
myimg.show()

# my cropped image
mybox = (0,0,400,400)
mynowimg = myimg.crop(mybox)
mynowimg.show()

#  conver the img 
myconvert = myimg.convert("1")
myconvert.show()