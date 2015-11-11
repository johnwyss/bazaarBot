#! /usr/bin/env python


from basic_agent import *
from agent_data import *
from inventory_data import *
from logic import *

class MarketData(object):
    def __init__(self, goods, agent_types, agents):
        """
        goods: a list of Good objects
        agent_types: a list of AgentData objects
        agents: a list of BasicAgent objects
        """
        self.goods = goods
        self.agent_types = agent_types
        self.agents = agents
	
	/**
	 * Parse a market settings file to construct everything
	 * @param	data		the JSON file definition for your Market
	 * @param	getAgent	a function to create agents
	 */
	
	public static function fromJSON(json:Dynamic, getAgent:AgentData->BasicAgent):MarketData
	{
		var goods:Array<Good> = [];
		
		//Create goods index
		var jsonGoods:Array<Dynamic> = json.goods;
		for (g in jsonGoods)
		{
			goods.push(new Good(g.id, g.size));
		}
		
		var agentTypes:Array<AgentData> = [];
		
		//Create agent classes
		var jsonAgents:Array<Dynamic> = json.agents;
		
		for (a in jsonAgents)
		{
			var agentData:AgentData = 
			{
				className:a.id,
				money:a.money,
				inventory:InventoryData.fromJson(a.inventory),
				logicName:a.id,
				logic:null
			}
			
			for (g in goods)
			{
				agentData.inventory.size.set(g.id, g.size);
			}
			
			agentTypes.push(agentData);
		}
		
		//Make the agent list
		var agents:Array<BasicAgent> = [];
		
		//Get start conditions
		var startConditions:Dynamic = json.start_conditions;
		var starts = Reflect.fields(startConditions.agents);
		
		var agentIndex:Int = 0;
		//Make given number of each agent type
		
		for (classStr in starts)
		{
			var val:Int = Reflect.field(startConditions.agents, classStr);
			var agentData = null;
			for (i in 0...agentTypes.length) {
				if (agentTypes[i].className == classStr)
				{
					agentData = agentTypes[i];
					break;
				}
			}
			
			for (i in 0...val)
			{
				var a:BasicAgent = getAgent(agentData);
				a.id = agentIndex;
				agentIndex++;
				agents.push(a);
			}
		}
		
		return new MarketData(goods, agentTypes, agents);
	}
}
