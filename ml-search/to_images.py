from PIL import Image 
import numpy as np
import os.path as path
import os
import json
import database
from io import BytesIO

color_map_path = path.join("data", "default_biome_profile.json")
color_map = dict(json.load(open(color_map_path))["colorMap"])
biome_num = 256
color_arr = np.zeros((biome_num, 3), dtype=np.uint8)
for i in range(biome_num):
    if i in color_map:
        color = color_map[i]
        color_arr[i, 0] = color["r"]
        color_arr[i, 1] = color["g"]
        color_arr[i, 2] = color["b"]

for world in database.World.select().where(database.World.image == None):
    biome_arr = np.load(BytesIO(world.biome_data))
    rgb = color_arr[biome_arr]
    rgb = rgb.transpose((1, 0, 2))
    f = BytesIO()
    Image.fromarray(rgb).save(f, format="png")
    database.World.update(image = f.getvalue()).where(database.World.seed == world.seed).execute()