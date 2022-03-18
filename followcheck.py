from PIL import ImageGrab, Image
import time

def ss():
    image = ImageGrab.grab()
    return image

def scanfollow():
    image = ss()
    data = image.load()
    a = []
    for i in range(1079):
        for j in range(1919):
            if(j<1700 and data[j,i] == (0,149,246) and data[j+140,i] == (0,149,246)):
                a.append(j)
                a.append(i)
                return a

def limitend():
    image = ss()
    data = image.load()
    if(data[912, 544] == (250, 139, 101)):
        return True
    else:
        return False

def checklikefail():
    image = ss()
    data = image.load()
    if data[921, 477] == (255, 52, 78):
        return True
    else:
        return False
    
#rgb(0,149,246)
