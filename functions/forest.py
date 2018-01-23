from mcpi.minecraft import Minecraft
mc = Minecraft.create()
count = 5
def growTree(x, y, z):
    mc.setBlock(x, y, z, 6)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
