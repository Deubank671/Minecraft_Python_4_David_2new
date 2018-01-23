from mcpi.minecraft import Minecraft
mc = Minecraft.craft()

block = 35
state = 6
mc.setBlocks(10, 3, -4, block, state)

mc.setBlocks(11, 3, -4, 20, 6, -8, block, state)

def getWoolState(color):
    if color == "pink":
        blockState = 6
        elif:
            
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(po.x, poy.y, pos.z, 35, state)
