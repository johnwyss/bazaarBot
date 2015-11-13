#! /usr/bin/env python

class InventoryData(object):
    def __init__(self, max_size, ideal, start, size):
        """max_size: float, ideal: dict of ideal commodities with number, start: dict, size: dict"""
        self.max_size = max_size
        self.ideal = ideal
        self.start = start
        self.size = size
        
    def from_json(self, data): # TODO: note this will probably not work.  needs some help
        maz_size = data.max_size
        ideal = {}
        start = {}
        size = {}
	
	    start_array = data.start
	    if start_array:
	        for s in start_array:
	            start[s] = data.start[s]
	            size[s] = 1 #initialize start of every item to 1 by default
	        
		ideal_array = data.ideal
		if ideal_array:
		    for i in ideal_array:
		        ideal[i] = data.ideal[i]
		        
		return InventoryData(max_size, ideal, start, size)
