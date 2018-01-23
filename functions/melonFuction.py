from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def makeMelon():  
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y - 1, z, 103)
    time.sleep(10)
    print ("make melon")
makeMelon()
makeMelon()
makeMelon()



