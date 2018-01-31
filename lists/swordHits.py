from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(60)

blockHits = mc.events.pollBlockHits()

blockHitsLength = blockHits
mc.postToChat("Your score is " + str(blockHitsLength))
