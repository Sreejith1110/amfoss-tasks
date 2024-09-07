# The Way To Read And Draw A Image Using Coordinates From Multiple Images Using lines.

computer languages used:
* Python

libraries used:
* Pillow
* Opencv
* Re(optional)
* Glob(optional)

## Introduction

In this post i am going to describe the way to read images and draw image using coordinates from multiple images with the help of _pillow_ and _opencv_ library in python. The programming is done in the _vs code_ platform.

## Technical Details

* Install _opencv_,_pillow_,_re_ and _glob_ in a virtual environment to avoid clashes between packages. After installing import each library into _vs code_ using the below codes.<br>
--> Opencv is used to open and read images in this program.It is imported using ___'import cv2'___.<br>
--> Pillow is used to create and draw images in this program. It is imported using ___'from PIL import Image, ImageDraw'___.<br>
--> Re is used to sort the images in ascending order of number in this program. It is imported using ___'import re'___. <br>
--> Glob is used to read each and every image names in a specific path given to it in this program. It is imported using ___'import glob'___.<br>

__* Step1__: Create a function to sort the image file using _re_ library.

	``def perfect(text):
              return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)',text)]``

__* Step2__: Create an empty image in a variable using _Image.new("RGB",(pixel),colour)_ function and we will use a variable to draw image inputing _ImageDraw.draw("empty image variable name")_.

	``image=Image.new("RGB",(512,512),"white")
          draw=ImageDraw.Draw(image)``

__* Step3__: Create two variable with value _None_ to start drawing line from the from the first coordinate we get.

	``x,y=None ,None``

__* Step4__: Create a variable for giving the image file names in a list form using _glob_ library and to sort the files number wise, use _glob.glob("path of the folder containing imaged"+"image name with extention")_ [In the program "_*.png_" signifies all the image with _png extention_] along with _key = function_ name and on that use _sorted_ function.

        ``img=sorted(glob.glob("/home/sreejith-m/Operation-Pixel-Merge/assets/"+'*.png'),key=perfect)``

__* Step5__: Using the for loop and cv2.imread() open each images in the path mentioned in the glob function.

	``for pic in img:
              picture=cv2.imread(pic)``
   
__* Step6__: Use _if_ and _else_ statement to check whether the image is valid or not missing any data to avoid errors.

	``if picture is None:
              print("none")
              continue
          else:``
           
__* Step7__: Calculate the dimension of the image using _shape()_ and store it in two variables.

	``height, width, _ = picture.shape``
	
__* Step8__: Create a variable with value 1 and create two _for loops_ using _range_ function of height and width of the image respectively as shown below.

	``a=1
          for i in range(height):
              for j in range(width):``

__* Step9__: Inside the _for loop_ check color of each pixel of image using __(B,G,R)__ and check if the color changes from the color that is been specified in __R,G,B__ format.[In this program white is the specified color]

	``(B, G, R)=picture[i, j]
          if(R != 255 or G != 255 or B != 255):``
                
__* Step10__: Inside the _if loop_ check whether the value of the variable used as the starting coordinate is _None_ and if it is _None_, change the value of the variable to the the first coordinate received from the _if loop_ from __Step9__ and change the value of the variable in __Step8__. Also use _break_ function to stop the _for loop_. [In the program __Step10__ helps to start image drawing at any coordinate which is returned by the _if loop_ in __Step9__]

        ``if x is None and y is None:
              x,y=i,j
              a=0
              break``
                
__* Step11__: If it is not _None_ then draw the line from the variables used as starting coordinates to the coordinate obtained from the image where the color changes from the specified color using _draw.line()_. Also change the value of the variable in __Step8__ and change the value of variable in __Step3__ to the value of the coordinate at the end of the line. Use _break_ function to stop the _loop_.
 
        ``else:
              vertices=[(x,y),(i,j)]
              draw.line(vertices,fill=(R,G,B),width=7)
              x,y=i,j
              a=0
              break``
                
__* Step12__: Outside the _for loops_ if the value of the variable in __Step8__ is still 1 then change the value of variable in __Step3__ to _None_.[In this program the __Step12__ is used to give spaces in the image when a blank or the specified colored image comes]

        ``if a ==1:
              x,y=None,None``

__* Step13__: Save the image using _variable_containing_image.save("image name")_

        ``image.save("amfoss.png")``
	
__* Step14__: If the image is rotated use *variable_containing_image.rotate(angle)_ and if the image is mirrored use *variable_containing_image.transpose(Image.FLIP_LEFT_RIGHT)* and then save in a variable.

        ``c=image.rotate(270)
          h = c.transpose(Image.FLIP_LEFT_RIGHT)``
	  
__* Step15__: Display the image using *image_name.show()*

	``h.show()``
	

## Conclusion

It introduces the world of creating , editing and drawing in images using python. Through the opencv and pillow it is possible to do that can be done in a image editor. It also familiarize us to other libraries like re and glob.
