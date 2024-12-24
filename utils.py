import os
import datetime
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


def callback(event):
    print("clicked at", event.x, event.y)


def getSegmentedImages(shape):
    parentDir = "segmentedImages/" + shape
    imagePaths = os.listdir(parentDir)
    imagePaths = [parentDir + "/" + _path for _path in imagePaths]
    return imagePaths

def getObscuredImages():
    imagePaths = os.listdir("obscuredImages")
    return imagePaths

def getGarbledImages():
    imagePaths = os.listdir("garbledImages")
    return imagePaths[:-1] # last file is txt file, don't need thats


def getCredentialImages():
    imagePaths = os.listdir("credentialImages")
    return imagePaths[:-1] # last file is txt file, don't need thats

class customImage:
    def __init__(self, path, width=200, height=150):
        self.path = path
        self.img_width = width
        self.img_height = height

    def draw(self, window, c_width=200, c_height=150, img_x=0, img_y=400):
        # Create a canvas
        canvas = Canvas(window, width=c_width, height=c_height)
        canvas.place(x=img_x, y=img_y)

        # Load an image in the script
        img = Image.open(self.path)

        # Resize the Image using resize method
        img = img.resize((self.img_width, self.img_height), Image.BICUBIC)
        img = ImageTk.PhotoImage(img)

        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=img)

        return canvas


class imageClick:
    def __init__(self, path):
        self.id = int(path[-5])
        self.path = path
        self.isClicked = False
        self.timeClicked = None

    def clicked(self, event):
        self.isClicked = True
        self.timeClicked = datetime.datetime.now()

        print("img id = ", self.id, " has been clicked")

    def __lt__(self, other):
        return self.timeClicked < other.timeClicked


def setAllUnclicked(imgClickedData):
    for obj in imgClickedData:
        obj.isClicked = False


def checkAllClicked(imgClickedData):
    for obj in imgClickedData:
        if obj.isClicked is False:
            return False

    return True


def create_popup(size="500x200", msg="default", font='Arial 24', x=140, y=70):
    win = Tk()
    win.geometry(size)
    win.title("Message")
    Label(win, text=msg, font=font).place(x=x, y=y)

    for i in range(300000):
        win.update_idletasks()
        win.update()

    win.destroy()
    return

import random
import string
from PIL import ImageDraw
from PIL import ImageFont

def generate_random_words(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_obscure_image(text):
    img = Image.new('RGB', (300, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    d.text((10, 10), text, fill=(0, 0, 0), font=font)
    img.save('obscure_image.png')
