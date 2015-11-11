#! /usr/bin/env python


class Good(object):
    def __init__(self, id='', size=1.0):
        """
        id: string id of good
        size: float of inventory size taken up
        """
        
        self.id = id
        self.size = size
    
    def copy(self):
        """ Be careful with this.  This will only work with immutable objects"""
        return Good(self.id, self.size)
        
