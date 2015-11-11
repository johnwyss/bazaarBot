#! /usr/bin/env python

# Converting this module to python
# going through one file at a time will have to edit all when finished

class Offer(object):
    """ 
    good: a string of the item offered
    units: the number of units
    unit_price: price per unit
    agent_id: the id of the agent making the offer
    """
    
    def __init__(self, agent_id=-1, good='', units=1.0, unit_price=1.0):
        self.agent_id = agent_id
        self.good = good
        self.units = units
        self.unit_price = unit price 
    
    def __str__(self):
        return '({}): {} x {} @ {}'.format(self.agent_id, self.good, self.units, self.unit_price)
