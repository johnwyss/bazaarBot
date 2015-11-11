#! /usr/bin/env python


from basic_agent import *



class Economy(object):
    def __init__(self):
        self.markets = []
        
    def add_market(self, m):
        """ takes a Market object """
        if self.markets
	"""
	public function addMarket(m:Market)
	{
		if (_markets.indexOf(m) == -1)
		{
			_markets.push(m);
			m.signalBankrupt.add(onBankruptcy);
		}
	"""
	    def get_market(self, name):
	    for m in self.markets:
	        if m.name == name:
	            return m
	            
	    def simulate(self, rounds):
	        for m in self.markets:
	            m.simulate(rounds)
	   
	   def on_bankruptcy(self, market, basic_agent):
	       pass # no implementation provide in subclass
