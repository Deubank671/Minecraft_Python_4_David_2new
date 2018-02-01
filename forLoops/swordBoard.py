from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}
while True:
    name = input("What's your name? ")
    mc.postToChat("Go!")
    time.sleep(60)
    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))
    scoreboard[name] = blockHitsLength

    for item in scoreboard:
        print(item + " " + str(scoreboard[item]))
   

    if name == "exit":
        break
    
    
