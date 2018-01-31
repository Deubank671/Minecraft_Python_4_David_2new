from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'snow': (6.6, 6.0, -8.5), 'sand': (5.3, -1.0, 14.3), 'grass': (28.7, 7.0, -33.7)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit to close'): ")
    if choice in places:
        location = places[choice]
        x, y, z = location
        mc.player.setTilePos(x, y, z)
        
