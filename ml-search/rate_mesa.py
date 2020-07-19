import numpy as np
from database import World
from io import BytesIO

mesa = [37, 39, 167, 38, 166, 165]

for world in World.select().where(World.biome_data.is_null(False)):
    arr = np.load(BytesIO(world.biome_data))
    if all(mesa_id not in arr for mesa_id in mesa):
        world.user_rating = 0
        world.save()