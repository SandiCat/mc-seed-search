from tkinter import *
import numpy as np
import os.path as path


fresh_seeds_dir = path.join("data", "fresh_seeds")
scores_dir = path.join("data", "scores")
world_cache_dir = path.join("data", "world_cache")

fresh_seeds_path = path.join(fresh_seeds_dir, "first_batch.txt")
scores_path = path.join(scores_dir, "first_batch.txt")

i = 0
fresh_seeds = open(fresh_seeds_path).read().splitlines()

root = Tk()
width = 1400
height = 650

canvas = Canvas(root, width = width, height = height)      
canvas.grid(column = 0, row = 0, columnspan = 5)

def load_world(seed):
    return np.load(path.join(world_cache_dir, f"{seed}.npy"))

def redraw(world):
    for x in range(width):
        for y in range(height):
            # color = "#" + "00ff00"
            color = "#" + hex(hash(world[x, y]))[2:].rjust(6, "0")
            canvas.create_line(x, y, x+1, y, fill=color)

redraw(load_world(fresh_seeds[i]))

slider = Scale(root, from_=0, to=1, resolution=-1, orient=HORIZONTAL, length=500)
slider.grid(column = 0, row = 1, columnspan = 3)

def next_btn_callback():
    global i
    with open(scores_path, "a") as scores_file:
        scores_file.write(f"{fresh_seeds[i]} {slider.get()}\n")
    i += 1
    new_seed = fresh_seeds[i]
    world = load_world(new_seed)
    redraw(world)


next_btn = Button(root, text = "next", command = next_btn_callback)
next_btn.grid(column = 3, row = 1)
save_btn = Button(root, text = "save", command = None)
save_btn.grid(column = 4, row = 1)

mainloop() 