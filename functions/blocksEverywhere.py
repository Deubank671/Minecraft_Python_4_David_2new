from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

blockType = 8

def randomBlockLocations(blockType, repeats):
    count = repeats
    while count > 0:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count -= 1
        print("works")
randomBlockLocations(8, 10)
        
       
