import jpype
import jpype.imports
from jpype.types import *

# Launch the JVM
jpype.startJVM(classpath=['amidst-v4-5-beta3.jar'])
import java.nio.file as file
mc = jpype.JPackage("amidst")
#inst_path = file.FileSystems.getDefault().getPath('/', 'home', 'sandi', '.local', 'share', 'multimc', 'instances', '1.16.1', '.minecraft')
inst = mc.mojangapi.file.MinecraftInstallation.newLocalMinecraftInstallation()
versions = list(inst.readInstalledVersionsAsLauncherProfiles())
prof = next(filter(lambda version: version.getVersionId() == '1.16.1', versions))
mc_interface = mc.mojangapi.minecraftinterface.MinecraftInterfaces.fromLocalProfile(prof)


seed = mc.mojangapi.world.WorldSeed.fromUserInput("hello")
world_type = mc.mojangapi.world.WorldType.DEFAULT
gen_opts = ""
opts = mc.mojangapi.world.WorldOptions(seed, world_type, gen_opts)
world = mc_interface.createWorld(seed.getLong(), world_type, gen_opts)
recognized_version = mc_interface.getRecognisedVersion()
builder = mc.mojangapi.world.versionfeatures.DefaultVersionFeatures.builder(opts, world)
features = builder.create(recognized_version)
biome_list = features.get(mc.mojangapi.world.versionfeatures.FeatureKey.BIOME_LIST)
biome_oracle = mc.mojangapi.world.oracle.BiomeDataOracle(world, recognized_version, biome_list)



from tkinter import *

root = Tk()
width = 1400
height = 650
canvas = Canvas(root, width = width, height = height)      
canvas.grid(column = 0, row = 0, columnspan = 2)
for x in range(width):
    for y in range(height):
        biome = biome_oracle.getBiomeAt(x, y, False)
        color = "#" + hex(hash(biome.getName()))[-6:]
        canvas.create_line(x, y, x+1, y, fill=color)

btn = Button(root, text = "yas queen", command = None)
btn.grid(column = 0, row = 1)
btn = Button(root, text = "yuck", command = None)
btn.grid(column = 1, row = 1)

mainloop()  