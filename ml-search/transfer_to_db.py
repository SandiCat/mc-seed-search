from database import *
import os
import os.path as path

def init():
    db.connect()
    db.create_tables([World])

def from_world_cache():
    db.connect()
    world_cache_dir = path.join("data", "world_cache")
    for filename in os.listdir(world_cache_dir):
        seed, ext = path.splitext(filename)
        data = open(path.join(world_cache_dir, filename), "rb").read()
        world = World.create(seed = int(seed), biome_data = data)