from mcpi.minecraft import Minecraft
mc = Minecraft.create()

twoDimentionalRainbowList = [[0, 0, 0],
                             [1, 1, 1],
                             [2, 2, 2],
                             [3, 3, 3],
                             [4, 4, 4],
                             [5, 5, 5]]

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
straightX = x
for row in twoDimentionalRainbowList:
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        x += 1
    y += 1
    x = straightX
  
     
        
    
