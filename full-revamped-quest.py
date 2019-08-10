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
server.vars.set("Magma_Leader", 5)
server.vars.set("Aqua_Leader", 6)

#ensuring player will be prompted by these msgs only once when visiting Mauville first time after beating Hoenn E4
#instead of being prompted every single step while walking on Mauville
if user.position.map == 'Mauville' and user.vars.HoennChamp and not user.vars.TransmatQuestDone and not user.vars.TransmatQuestStarted:
    user.say('...')
    user.say('.......')
    user.say('...Why am I getting the feeling I must speak to Mauville Poke Center Secure Officer...?')
    user.say("I'd better reach out to him right now")
    user.pause()
    user.vars.set("TransmatQuestStarted", True)


#Secure Officer interaction
#refine these npc text messages
if user.vars.interaction_secure_office:
    user.say("What you waiting for?! I have no further informations.")
    user.pause()
else:   
    user.say('You must reach towards New Mauville as soon as possible!')
    user.say('Hoenn Transmat System stopped to work for unknow reasons, but we have already detected that Team Magma \\
            and Aqua are involved on that.')
    user.say("Also, they seem to be working on a plan to break the whole communication system in order to replace with \\
            their software. This would turn the Hoenn Transmat system to be completely under these evil corporation's control!")
    user.say("Watson is stading on New Mauville holding more useful information regarding all this situation. Go to see him.")
    user.pause()
    user.vars.set("interaction_secure_office", True)


#Watson interaction, catching Plusle and Minun
#add here more npc storytelling text message
if user.vars.TradeWattson #I didnt wanna use a number for an existing NPC, so I used a name
    user.say("Thank you so much for your help!")
    user.say('You must defeat Wally and May on a battle, so they can help you to reach \\
            the Poke Centers and install the countermeasure software faster!')

user.say('You must catch a Plusle and Minun, so that I can charge those generators up again and attempt by \\
        myself some sort of temporary workaround for Transmat System!')
choice = user.select("Did you bring me my precious Plusle and Minun?", ["Yes.", "No"])
if choice[0] == 1:
    return user.say("Please hurry!.")

#If the pokemon is not Plusle/Minun and not your OT
poke = user.select_pokemon("Select your Plusle/Minun")
if poke.name != "Plusle" or poke.name !="Minun" or poke.ot != user.username:
    return user.say("You didn't find that pokemon!")

del user.pokes[poke.pos]

user.say("Thank you so much!!")
user.pause()
user.var.TradeWattson = 1

#Making Wally and May appear for player interaction after finishing Plusle and Minun hunting
npcs[2].id == server.vars.May
npcs[3].id == server.vars.Wally
npcs[2].hide, npcs[3].hide = False


#Wally and May interaction and Battle

#list of cities
hoenn_cities = ['Littleroot','Oldale','Petalburg','Rustboro','Dewford','Slateport','Mauville','Verdanturf','Fallarbor','Lavaridge','Fortree','Lilycove','Mossdeep','Sootopolis','Pacifidlog','Ever Grande']

user.say("Wally: Show me you've got that really strong enough to make both of us work together against these bad guys gangs!")
user.pause()
npcs[2].team = [Pokemon("Altaria", 75), Pokemon("Roserade", 75), Pokemon("Aggron", 75), Pokemon("Mega Gallade", 75)]
npcs[3].team = [Pokemon("Swellow", 75), Pokemon("Magcargo", 75), Pokemon("Togekiss", 75), Pokemon("Slaking", 75)]
result = user.battle(npcs[2])
#in case winning Wally, battle sequentially May
if result == 1:
    user.say("May: Wally, will only move a finger if you also defeat me {}, bring it on!".format(user.username))
    result = user.battle(npcs[3])
    if result == 1:
        #routine for random selected Hoenn PC
        choosen_cities = [hoenn_cities.pop(random.randrange(len(hoenn_cities))) for counter in range(3)]
        user.say("May: Fair enough, we will be heading to {} and {} as fast as we can. {}, do the \\
                same right now!".format(choosen_cities[0], choosen_cities[1], user.username))
        user.say("Hurry to {}!".format(choosen_cities[2]))
        user.pause()
        #making them disappear
        npcs[2].hide, npcs[3].hide = True


#Interacting to PC computer
if user.vars.interaction_transmat_computer:
    user.say("The computer seems running fine with countermeasure software installed.")
    user.pause()
else:
    user.say("You've installed the countermeasure software in that system!")
    user.say("{}: Great! As soon May and Wally perform the same installation, Transmat Hoenn System \\
            will power on again!".format(user.username))
    user.say("{}: It's better I get back to Watson and tell him to be aware for any unexpected situation \\
            while system is brought back...".format(user.username))
    user.pause()
    user.vars.set("interaction_transmat_computer", True)


#Interacting NPCs Team Aqua/Magma Leaders
#detect here if user position is the squares around room's exit, it will trigger showing Gang Leaders event

#showing Team Leaders
npcs[5].id == server.vars.Magma_Leader
npcs[6].id == server.vars.Aqua_Leader
npcs[5].hide, npcs[6].hide = False
#SOMEONE DEFINE A DIFFERENT TEAM HERE, PLEASE XD
npcs[5].team = [Pokemon("Swellow", 75), Pokemon("Magcargo", 75), Pokemon("Togekiss", 75), Pokemon("Slaking", 75)]
npcs[6].team = [Pokemon("Swellow", 75), Pokemon("Magcargo", 75), Pokemon("Togekiss", 75), Pokemon("Slaking", 75)]
user.say("Team Magma Leader: You won't go that far, kid!")
user.say("Team Aqua Leader: We arrived at the exactly time to kick you out and install a new software \\
        on computer to make Transmat system completely owned for Team Aqua and Magma!")
user.say("Team Magma/Aqua Leader: We will take it over once for all!")
user.say("Team Magma Leader: Get yourself ready now and let's battle, me first!")
user.pause()
#routine for Battling Team Aqua and Magma Leaders
result = user.battle(npcs[5])
if result == 1:
    user.say("Team Aqua: Don't think we are done, battle now!")
    result = user.battle(npcs[6])
    if result == 1:
        user.say("Team Aqua Leader: No! Can't believe our plans are being delayed by that kid again.")
        user.say("Team Magma Leader: It's not the end, we are bigger and stronger than you've seen here now")
        user.say("Team Magma/Aqua Leaders: Save our words, we will be back in the future!")
        user.pause()
        #making them disappear
        npcs[5].hide, npcs[6].hide = True
        #teleport player to New Mauville space in front of Watson

        #final dialog to end quest, Watson Interaction
        user.say("Watson: Thank you kind, Transmat System is available again!")
        user.say("Watson: Beyond you're being able to use the system whenever you want hence and forth, receive that reward as \\
                my gratitude for your performace to save Mauville and Hoenn entirely")
        user.pause()
        user.items['Big Nugget'] = user.items['Big Nugget'] + 1 #maybe it's not a fair item for all those battles? XD
        user.vars.TransmatQuestDone = True
else: 
    #condition in case player lose battle
