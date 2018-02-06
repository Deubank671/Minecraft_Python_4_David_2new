from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
for temp in range(1, 50):
    blockType = mc.getBlock(x, y - temp, z)
    if blockType == 56:
        mc.postToChat("Great a diamond ore is below you!!")
        mc.postToChat("The block is " + str(temp) + " below you")
        break
    else:
        mc.postToChat("Keep looking for diamond ore")

