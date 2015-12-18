"""
brit.py - Phenny Rude Module
Copyright 2012, lunar
Licensed under the Eiffel Forum License 2.
http://inamidst.com/phenny/
This is a nano function to call random British swears into an IRC channel.  
"""
import random

swears = ["Your mom's a slag faggot!", 
	  "Wank my ass in your face cunt!", 
	  "Rude!", 
	  "You binbongy cunt, go drink your mom's tats you fag!", 
	  "You're such a uphill gardener you queer!",
          "Fuck your shit, Amerifat.", 
          "I'm gonna go drink tea with Dark, because we're British #swagger."]
          #You can also define your own rude swears here!

def brit(phenny, input):
	rude = "%s" % str(random.choice(swears))
	phenny.say(rude)
brit.commands = ['brit']
brit.priority = 'high'
