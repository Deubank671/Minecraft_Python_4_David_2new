from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    mc.setBlock(x, y, z, block)
    return block

pos = mc.player.getTilePos()    
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10



for height in range(5):
    brokenWall.append([])
    for width in range(10):
        brokenBlocks = [48, 67, 4, 4, 4, 4]
        block = random.choice(brokenBlocks)
        brokenWall[height].append(block)
for row in brokenWall:
    for item in row:
        mc.setBlock(x, y, z, item)
        x += 1
    y += 1
    x = pos.x




