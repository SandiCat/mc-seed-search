from tkinter import *
import numpy as np
from database import World
from PIL import Image, ImageTk
from io import BytesIO

root = Tk()

label = Label(root)
label.grid(column = 0, row = 0, columnspan = 5)

current_world = None

def next_world():
    global current_world, label
    current_world = World.select().where(World.user_rating.is_null(True) & World.image.is_null(False)).get()
    image = Image.open(BytesIO(current_world.image))
    photo_image = ImageTk.PhotoImage(image)
    label.config(image=photo_image)
    label.image = photo_image

next_world()

slider = Scale(root, from_=0, to=1, resolution=-1, orient=HORIZONTAL, length=500)
slider.grid(column = 0, row = 1, columnspan = 3)

def next_btn_callback():
    current_world.user_rating = slider.get()
    current_world.save()
    next_world()


next_btn = Button(root, text = "next", command = next_btn_callback)
next_btn.grid(column = 3, row = 1)

def save_btn_callback():
    current_world.saved = True
    current_world.save()

save_btn = Button(root, text = "save", command = save_btn_callback)
save_btn.grid(column = 4, row = 1)

mainloop() 