from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

block = [20, 20, 20, 20, 20, 20, 20, 20, 20]
block.append(20)


barBlock = 22

count= 0
while count <= len(block):
    mc.setBlock(x, y, z, block[0])
    mc.setBlock(x, y + 1, z, block[1])
    mc.setBlock(x, y + 2, z, block[2])
    mc.setBlock(x, y + 3, z, block[3])
    mc.setBlock(x, y + 4, z, block[4])
    mc.setBlock(x, y + 5, z, block[5])
    mc.setBlock(x, y + 6, z, block[6])
    mc.setBlock(x, y + 7, z, block[7])
    mc.setBlock(x, y + 8, z, block[8])
    mc.setBlock(x, y + 9, z, block[9])

    count +=1
    del block[0]
    block.insert(0, barBlock)
    mc.setBlock(x, y, z, block[0])
    time.sleep(2)
    del block[1]
    block.insert(1, barBlock)
    mc.setBlock(x, y + 1, z, block[1])
    time.sleep(2)
    del block[2]
    block.insert(2, barBlock)
    mc.setBlock(x, y + 2, z, block[2])
    time.sleep(2)
    del block[3]
    block.insert(3, barBlock)
    mc.setBlock(x, y + 3, z, block[3])
    time.sleep(2)
    del block[4]
    block.insert(4, barBlock)
    mc.setBlock(x, y + 4, z, block[4])
    time.sleep(2)
    del block[5]
    block.insert(5, barBlock)
    mc.setBlock(x, y + 5, z, block[5])
    time.sleep(2)
    del block[6]
    block.insert(6, barBlock)
    mc.setBlock(x, y + 6, z, block[6])
    time.sleep(2)
    del block[7]
    block.insert(7, barBlock)
    mc.setBlock(x, y + 7, z, block[7])
    time.sleep(2)
    del block[8]
    block.insert(8, barBlock)
    mc.setBlock(x, y + 8, z, block[8])
    time.sleep(2)
    del block[9]
    block.insert(9, barBlock)
    mc.setBlock(x, y + 9, z, block[9])
    time.sleep(2)
    break
   
    
