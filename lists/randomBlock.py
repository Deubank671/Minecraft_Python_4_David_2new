from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

blocks = 63, 57, 18
blockType = random.choice(blocks)
pos = mc.player.getTilePos()
print(random.choice(blocks))

mc.setBlock(pos.x, pos.y, pos.z, blockType)
