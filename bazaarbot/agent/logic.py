#! /usr/bin/env python


import json
import random

class Logic(object):
    def __init__(self, data=None):
        self.init = False
        # no implementation -- provide your own in a subclass
    
    # perform this logic on the given agent
    def perform(self, agent, market):
        """agent:BasicAgent object, market:Market object"""
        pass #no implemenation -- provide your own in a subclass
	
	def produce(self, agent, commodity, amount, chance=1.0):
	    if (chance >= 1.0) or (random.random() < chance):
	        agent.change_inventory(commodity, amount)
	
    def consume(self, agent, commodity, amount, chance = 1.0):
        if (chance >= 1.0) or (random.random() < chance):
            if commodity == "money":
                agent.money -= amount
            else:
                agent.change_inventory(commodity, -amount) # if money was a commodity this would not be needed
