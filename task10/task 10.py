from PIL import Image, ImageDraw
import cv2
import glob
import re


def perfect(text):
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)',text)]


image=Image.new("RGB",(512,512),"white")
draw=ImageDraw.Draw(image)
x,y=None ,None
img=sorted(glob.glob("/home/sreejith-m/Operation-Pixel-Merge/assets/"+'*.png'),key=perfect)
for pic in img:
    picture=cv2.imread(pic)
    if picture is None:
        print("none")
        continue
    else:
        height, width, _ = picture.shape
        a=1
        for i in range(height):
            for j in range(width):
                (B, G, R)=picture[i, j]
                if(R != 255 or G != 255 or B != 255):
                    if x is None and y is None:
                        x,y=i,j
                        a=0
                        break
                        
                    else:
                        vertices=[(x,y),(i,j)]
                        draw.line(vertices,fill=(R,G,B),width=7)
                        x,y=i,j
                        a=0
                        break
        if a ==1:
            x,y=None,None  
            a=1         
image.save("amfoss.png")
c=image.rotate(270)
h = c.transpose(Image.FLIP_LEFT_RIGHT)
h.show()