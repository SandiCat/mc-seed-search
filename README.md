# mc-seed-search

![](https://i.imgur.com/7F83R4v.png)

Generate Minecraft worlds en masse while filtering for desired biomes, then grade the worlds on a scale from 0 to 1 with a handy GUI. The grades will be used to train a convolutional neural net to automate the seed search process (this part isn't done yet).

This was created in the span of a few days for my girlfriend, so the code quality is not high and the software is not polished to the point where it's easy to use. There's a lot of superfluous code files from experimentation. If you want to use it for yourself and run into problems, shoot me a message.

Implemented in Python. Uses Tkinter for the GUI, numpy and pillow for generating maps of the worlds, JPype for communicating with Java code that implements Minecraft world generation and peewee in conjuction with a sqlite database for persistent storage.

## Usage

Requires a Minecraft 1.16.1 installation (desired version can be easily changed). Communication with Minecraft is done through [Amidst](https://github.com/toolbox4minecraft/amidst), so an Amidst binary needs to be placed at `assets/amidst-v4-5-beta3.jar` (can be downloaded [here](https://github.com/toolbox4minecraft/amidst/releases/tag/v4.5-beta3)).

Python packages can be installed with `pip install -r requirements.txt`. You might want to create a virtual env for that.

**Seed generation:** `python generate_seeds.py`, `Ctrl+C` to stop generating.

**Image generation:** Images need to be generated from the biome data for the worlds. Do that with `python to_images.py`. This might take a while.

**Seed grading:** `python grading_gui.py` will bring up a simple GUI for grading the worlds.
