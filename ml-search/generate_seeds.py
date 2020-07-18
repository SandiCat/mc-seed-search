import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=['amidst-v4-5-beta3.jar'])
import java.nio.file as file
mc = jpype.JPackage("amidst")
#inst_path = file.FileSystems.getDefault().getPath('/', 'home', 'sandi', '.local', 'share', 'multimc', 'instances', '1.16.1', '.minecraft')
inst = mc.mojangapi.file.MinecraftInstallation.newLocalMinecraftInstallation()
versions = list(inst.readInstalledVersionsAsLauncherProfiles())
prof = next(filter(lambda version: version.getVersionId() == '1.16.1', versions))
mc_interface = mc.mojangapi.minecraftinterface.MinecraftInterfaces.fromLocalProfile(prof)
builder = mc.mojangapi.world.WorldBuilder.createSilentPlayerless()


import numpy as np

width = 1400
height = 650

import os.path as path
fresh_seeds_dir = path.join("data", "fresh_seeds")
world_cache_dir = path.join("data", "world_cache")
filename = path.join(fresh_seeds_dir, "first_batch.txt")

with open(filename, "a") as seeds_file:
    for i in range(1000):
        seed = mc.mojangapi.world.WorldSeed.random()
        world_type = mc.mojangapi.world.WorldType.DEFAULT
        gen_opts = ""
        opts = mc.mojangapi.world.WorldOptions(seed, world_type, gen_opts)
        world = builder.from_(mc_interface, opts)
        biome_oracle = world.getBiomeDataOracle()

        def biome_val(x, y):
            return np.uint8(int(biome_oracle.getBiomeAt(x, y, True).getId()))

        world = np.fromfunction(np.vectorize(biome_val), (width, height), dtype=np.int64)
        np.save(path.join(world_cache_dir, f"{seed.getLong()}.npy"), world)
        seeds_file.write(f"{seed.getLong()}\n")
        print(i, seed.getLong())