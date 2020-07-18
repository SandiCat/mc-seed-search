from PIL import Image 
import numpy as np
import os.path as path
import os
import json

fresh_seeds_dir = path.join("data", "fresh_seeds")
scores_dir = path.join("data", "scores")
world_cache_dir = path.join("data", "world_cache")
image_dir = path.join("data", "images")

color_map = dict(json.load(open("default_biome_profile.json"))["colorMap"])
biome_num = 256
color_arr = np.zeros((biome_num, 3), dtype=np.uint8)
for i in range(biome_num):
    if i in color_map:
        color = color_map[i]
        color_arr[i, 0] = color["r"]
        color_arr[i, 1] = color["g"]
        color_arr[i, 2] = color["b"]

for filename in os.listdir(world_cache_dir):
    seed, ext = path.splitext(filename)
    world = np.load(path.join(world_cache_dir, filename))
    rgb = color_arr[world]
    rgb = rgb.transpose((1, 0, 2))
    Image.fromarray(rgb).save(path.join(image_dir, seed + ".png"))