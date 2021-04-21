# it3038c-scripts
  
Project 3

  This code is using the Pillow module to take images from the internet at URLs and edit them within the code. 
  NOTE: Please use a file under 600x500 or you will experience problems.
  
  Make sure to install Pillow(pip install pillow).
  
  When you run the code it will ask you to paste a URL of an image. Make sure the URL ends with .png, .jpg or .jpeg.
  
    userinput = input("Paste a link of an image you want to edit. ")
    
  You will get a printed line of the dimensions of your image and the file type. This is there so you know your on the right track! Ex: PNG (512, 512) RGB
  
  It wil then ask if you want to Rotate, Flip, Deepfry or Smooth the image.
  
    userinput1 = input("Do you want to Rotate the image, Flip the image(horizontally), Deepfry the image or Smooth the image? ")
    
  Write flip, rotate, deepfried or smooth. (capitalization does not matter).
  
  Once you enter your choice you will get a message asking you to wait based on how long your image takes to render. 
  I tested these out with an HD file in the correct image proportions I said earlier.(600x500)
  
  This will then cause the image to be displayed in whatever your default browser for your machine is. 
  
    img.show()
  
  Then theres a small message at the bottom, answer yes or no or whatever, it's just there for fun.
  
  This is how you use my code! Enjoy it!
