# this project works with image processing 

import cImage as image

img = image.Image("luther.gif")
w=img.getWidth()


h=img.getHeight()
newimg = image.EmptyImage(w,h)
win = image.ImageWin()

for i in range(w):
    for j in range(h):
        pix = img.getPixel(i, j)

        newred = 0
        green = pix.getGreen()
        blue = pix.getBlue()

        newpixel = image.Pixel(newred, green, blue)

        newimg.setPixel(i, j, newpixel)

newimg.draw(win)

win.exitonclick()


#Convert the image to grayscale.
def convertgrayscale(inpImg):
    gray_image = image.EmptyImage(inpImg.getWidth(), inpImg.getHeight())

    for col in range(inpImg.getWidth()):
        for row in range(inpImg.getHeight()):
            p = inpImg.getPixel(col, row)

            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            avg = (red + green + blue)//3

            newpixel = image.Pixel(avg, avg, avg)
            gray_image.setPixel(col, row, newpixel)

    return gray_image


win = image.ImageWin()
img = image.Image("luther.gif")

gray_img = convertgrayscale(img)
gray_img.draw(win)

win.exitonclick()
   

#Function to convert an image to sepia tone.
def convertSepia(inImg):
    sepia_img=image.EmptyImage(inImg.getWidth(),inImg.getHeight())

    for col in range(inImg.getWidth()):
        for row in range(inImg.getHeight()):
            p=inImg.getPixel(col,row)

            R=p.getRed()
            G=p.getGreen()
            B=p.getBlue()
            newR = int(R * 0.393 + G * 0.769 + B * 0.189)
            newG = int(R * 0.349 + G * 0.686 + B * 0.168)
            newB = int(R * 0.272 + G * 0.534 + B * 0.131)

            newpixel = image.Pixel(newR, newG, newB)
            sepia_img.setPixel(col, row, newpixel)

    return sepia_img


win = image.ImageWin()
img = image.Image("luther.gif")

sepia_img = convertSepia(img)
sepia_img .draw(win)

win.exitonclick()

            




#Function to uniformly enlarge an image by a factor of 2 (double the size).
def double_size(oldImg):
    new_Img = image.EmptyImage(oldImg.getWidth()*2,oldImg.getHeight()*2)
    for row in range(oldImg.getHeight()):
        for col in range(oldImg.getWidth()):
            p=oldImg.getPixel(col,row)
            
            new_Img.setPixel(2*col, 2*row, p)
            new_Img.setPixel(2*col+1, 2*row, p)
            new_Img.setPixel(2*col, 2*row+1, p)
            new_Img.setPixel(2*col+1, 2*row+1, p)

    return new_Img

win = image.ImageWin()
img = image.Image("luther.gif")

double_Img = double_size(img)
double_Img.draw(win)

win.exitonclick()



#Function that takes an image as a parameter and smooths the image since 
# making it large can blur it out 
def double_size(inImg):
    new_Img = image.EmptyImage(inImg.getWidth()*2,inImg.getHeight()*2)
    for row in range(new_Img.getHeight()):
        for col in range(new_Img.getWidth()):
            
            v0=new_Img.getPixel(col*2,row*2)
            v1=new_Img.getPixel(col*2+1,row*2)
            v2=new_Img.getPixel(col*2,row*2+1)
            v3=new_Img.getPixel(col*2+1,row*2+1)
            v4=new_Img.getPixel(col*2,row*2)
            v5=new_Img.getPixel(col*2+1,row*2)
            v6=new_Img.getPixel(col*2,row*2+1)
            v7=new_Img.getPixel(col*2+1,row*2+1)

            newRed=(v0.getRed()+v1.getRed()+v2.getRed()+v3.getRed()+v4.getRed()+v5.getRed()+v6.getRed()+v7.getRed())//8
            newGreen=(v0.getGreen()+v1.getGreen()+v2.getGreen()+v3.getGreen()+v4.getGreen()+v5.getGreen()+v6.getGreen()+v7.getGreen())//8
            newBlue=(v0.getBlue()+v1.getBlue()+v2.getBlue()+v3.getBlue()+v4.getBlue()+v5.getBlue()+v6.getBlue()+v7.getBlue())//8

            v=image.Pixel(newRed,newGreen,newBlue)
            new_Img.setPixel(col,row,v)
                            
    return new_Img

win = image.ImageWin()
img = image.Image("luther.gif")

double_Img = double_size(img)
double_Img.draw(win)

win.exitonclick()



