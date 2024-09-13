# Explaination about task 10
* Step1: Create a function to sort the image file using re library.

``def perfect(text):
          return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)',text)]``
* Step2: Create an empty image in a variable using Image.new("RGB",(pixel),colour) function and we will use a variable to draw image inputing ImageDraw.draw("empty image variable name").

``image=Image.new("RGB",(512,512),"white")
      draw=ImageDraw.Draw(image)``
* Step3: Create two variable with value None to start drawing line from the from the first coordinate we get.

``x,y=None ,None``
* Step4: Create a variable for giving the image file names in a list form using glob library and to sort the files number wise, use glob.glob("path of the folder containing imaged"+"image name with extention") [In the program "*.png" signifies all the image with png extention] along with key = function name and on that use sorted function.

    ``img=sorted(glob.glob("/home/sreejith-m/Operation-Pixel-Merge/assets/"+'*.png'),key=perfect)``
* Step5: Using the for loop and cv2.imread() open each images in the path mentioned in the glob function.

``for pic in img:
          picture=cv2.imread(pic)``
* Step6: Use if and else statement to check whether the image is valid or not missing any data to avoid errors.

``if picture is None:
          print("none")
          continue
      else:``
* Step7: Calculate the dimension of the image using shape() and store it in two variables.

``height, width, _ = picture.shape``
* Step8: Create a variable with value 1 and create two for loops using range function of height and width of the image respectively as shown below.

``a=1
      for i in range(height):
          for j in range(width):``
* Step9: Inside the for loop check color of each pixel of image using (B,G,R) and check if the color changes from the color that is been specified in R,G,B format.[In this program white is the specified color]

``(B, G, R)=picture[i, j]
      if(R != 255 or G != 255 or B != 255):``
* Step10: Inside the if loop check whether the value of the variable used as the starting coordinate is None and if it is None, change the value of the variable to the the first coordinate received from the if loop from Step9 and change the value of the variable in Step8. Also use break function to stop the for loop. [In the program Step10 helps to start image drawing at any coordinate which is returned by the if loop in Step9]

    ``if x is None and y is None:
          x,y=i,j
          a=0
          break``
* Step11: If it is not None then draw the line from the variables used as starting coordinates to the coordinate obtained from the image where the color changes from the specified color using draw.line(). Also change the value of the variable in Step8 and change the value of variable in Step3 to the value of the coordinate at the end of the line. Use break function to stop the loop.

    ``else:
          vertices=[(x,y),(i,j)]
          draw.line(vertices,fill=(R,G,B),width=7)
          x,y=i,j
          a=0
          break``
* Step12: Outside the for loops if the value of the variable in Step8 is still 1 then change the value of variable in Step3 to None.[In this program the Step12 is used to give spaces in the image when a blank or the specified colored image comes]

    ``if a ==1:
          x,y=None,None``
* Step13: Save the image using variable_containing_image.save("image name")

    ``image.save("amfoss.png")``
* Step14: If the image is rotated use *variable_containing_image.rotate(angle)_ and if the image is mirrored use variable_containing_image.transpose(Image.FLIP_LEFT_RIGHT) and then save in a variable.

    ``c=image.rotate(270)
      h = c.transpose(Image.FLIP_LEFT_RIGHT)``
* Step15: Display the image using image_name.show()

``h.show()``
