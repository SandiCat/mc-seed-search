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


seed = mc.mojangapi.world.WorldSeed.fromUserInput("hello")
world_type = mc.mojangapi.world.WorldType.DEFAULT
gen_opts = ""
opts = mc.mojangapi.world.WorldOptions(seed, world_type, gen_opts)
world = builder.from_(mc_interface, opts)
biome_oracle = world.getBiomeDataOracle()


import numpy as np

width = 1400
height = 650
def biome_val(x, y):
    return int(biome_oracle.getBiomeAt(x, y, False).getId())
world = np.fromfunction(np.vectorize(biome_val), (width, height), dtype=int)
