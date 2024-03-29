import urllib.request
import sys, os
import time
from PIL import Image
from PIL import ImageFilter

#example of python user input, introducing to a user what the program does without reading the README
print("This is a program to edit images from URLs.") 
userinput = input("Paste a link of an image you want to edit. ")

#using pillow to save the requested image and save in in the current directory
im = urllib.request.urlretrieve(userinput, "sample.png")
im = Image.open("sample.png")
print(im.format, im.size, im.mode)

#take the image and manipulate it for you to view, i used the time function to allow the image to be rendered as a temporary BMP file
userinput1 = input("Do you want to Rotate the image, Flip the image(horizontally), Deepfry the image or Smooth the image? ")
if (userinput1 == "rotate") or (userinput1 == "Rotate"):
    img = im.transpose(Image.ROTATE_90)
    print("Please wait 45 seconds for your image to render.")
    time.sleep(45)
    img.show()
elif (userinput1 == "flip") or (userinput1 == "Flip"):
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    print("Please wait 30 seconds for your image to render.")
    time.sleep(30)
    out.show()
elif (userinput1 == "smooth") or (userinput1 == "Smooth"):
    im_blur = im.filter(ImageFilter.SMOOTH)
    print("Please wait 40 seconds for your image to render.")
    time.sleep(40)
    im_blur.show()
elif (userinput1 == "Deepfried") or (userinput1 == "deepfried"):
    im_edge = im.filter(ImageFilter.FIND_EDGES)
    print("Please wait 30 seconds for your image to render.")
    time.sleep(30)
    im_edge.show()
else:
    print("Bye!")

#i spent a fair amount of time trying to figure out how to save it to desktop on windows before i realized people used Linux machines in our class
userinput2 = input("Are you doing ok today? ")
if (userinput1 == "yes") or (userinput1 == "Yes"):
    print("Good! Because you don't get to keep the image.")
else:
    print("Thats too bad...I'm sorry I can't cheer you up by letting you keep the image. :P ")
