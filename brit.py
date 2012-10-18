"""
brit.py - Phenny Rude Module
Copyright 2012, Captain Lunar 
Licensed under the Eiffel Forum License 2.
http://sites.google.com/site/captainlunarlabs/

http://inamidst.com/phenny/
"""
#This is a nano function to call random British swears
#into the IRC channel on command. 

import random

swears = ["Your mom's a slag faggot!", "Wank my ass in your face cunt!", "Rude!", "You binbongy cunt, go drink your mom's tats you fag!", "You're such a uphill gardener you queer!",
         "Fuck your shit, Amerifat.", "I'm gonna go drink tea with Dark, because we're British #swagger."]

def brit(phenny, input):
	rude = "%s" % str(random.choice(swears))
	phenny.say(rude)
brit.commands = ['brit']
brit.priority = 'high'
