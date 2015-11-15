#! /usr/bin/env python

from market import *
from agent import *


class LogicHScript(Logic)

	var script:String = "";
	var source:String;
	
	def __init__(self, data=None):
	    if not data:
	        return None # this wont work in python
	    super.__init__(data)
	    script = Assets.get_text('assets/scripts/'+data)
	
	def perform(self, agent, bazaar):
	    self.perform_script(script, agent, bazaar)
	    
	def perform_script(self, script, agent, bazaar):
	    parser = Parser()
	    ast = parser.parse_string(script)
	    interp = Interp()
        
        _vars = {}
        _vars['agent'] = agent
        _vars['query_inventory'] = agent.query_inventory
        _vars['produce'] = self.produce
        _vars['consume'] = self.consume
        _vars['inventory_is_full'] = agent.get_inventory_full
        _vars['make_room_for'] = 
        """
			function(a:Agent, c:String = "food", amt:Float = 1.0):Void
			{ 
				var to_drop:String = bazaar.getCheapestCommodity(10, [c]);
				if (to_drop != "") {_consume(a, to_drop, amt);}
			}
		""" # do not understand this part
	   ast() # not sure if this is correct

