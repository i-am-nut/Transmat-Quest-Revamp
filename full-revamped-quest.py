#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""
Maybe rip the code in different scripts for each specific interaction and routine?
"""

from PRO_API import *
import random
from datetime import datetime

server.vars.set("Watson", 1)
server.vars.set("May", 2)
server.vars.set("Wally", 3)
server.vars.set("Mauville_Secure_Officer", 4)

if user.position.map == 'Mauville' and user.vars.HoennChamp and not user.vars.TransmatQuestDone:
    user.say('...')
    user.say('.......')
    user.say('...Why am I getting the feeling I must speak to Mauville Poke Center Secure Officer...?')
    user.say("I'd better reach out to him right now")
    user.pause()


#Secure Officer interaction
"""
refine npc text messages
"""
user.say('You must reach towards New Mauville as soon as possible!')
user.say('Hoenn Transmat System stopped to work for unknow reasons, but we have already detected that Team Magma \\
        and Aqua are involved on that.')
user.say("Also, they seem to be working on a plan to break the whole communication system in order to replace with \\
        their software. This would turn the Hoenn Transmat system to be completely under these evil corporation's control!")
user.say("Watson is stading on New Mauville holding more useful information regarding all this situation. Go to see him.")
 
#Watson interaction, catching Plusle and Minun
"""
add here more npc storytelling text message
"""
user.say('You must catch a Plusle and Minun, so that I can charge those generators up again and attempt by \\
        myself some sort of temporary workaround for Transmat System!')
"""
catching Plusle and Minun routine and messages here
"""

if user.vars.PlusleMinunCaught:
    user.say('You must defeat Wally and May on a battle, so they can help you to reach \\
            the Poke Centers and install countermeasure software faster!')

#Wally and May interaction and Battle
"""
define a list of Hoenn cities and select two random ones for May and Wally and one for us.
"""
npcs[2].id == server.vars.May
npcs[3].id == server.vars.Wally
npcs[2].hide, npcs[3].hide = False
user.say("Waly: Show me you've got that really strong enough to both of us work together against these bad guys gangs!")
npcs[2].team = [Pokemon("Altaria", 75), Pokemon("Roserade", 75), Pokemon("Aggron", 75), Pokemon("Mega Gallade", 75)]
npcs[3].team = [Pokemon("Swellow", 75), Pokemon("Magcargo", 75), Pokemon("Togekiss", 75), Pokemon("Slaking", 75)]
result = user.battle(npcs[2])
if result == 1:
    user.say("May: Wally will only move a finger if you also defeat me {}, bring it on!".format(user.username))
    result = user.battle(npcs[3])
    if result == 1:
        user.say("May: Fair enough, we will be heading to {} and {} as fast as we can {}, do the \\
                same right now!".format(randomcity1, randomcity2, user.username))
        npcs[2].hide, npcs[3].hide = True

#routine for random selected Hoenn PC

#routine for Battling Team Aqua and Magma Leaders

#final routine to end quest

