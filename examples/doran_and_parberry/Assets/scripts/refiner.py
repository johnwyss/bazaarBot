#! /usr/bin/env python

food = query_inventory('food')
tools = query_inventory('tools')
ore = query_inventory(ore')
	
has_food = food >= 1
has_tools = tools >= 1
has_ore = ore >= 1

if has_food and has_ore:
    if has_tools:
        # Convert all ore into metal, consume 1 food, break tools with 10% chance
        produce(agent, 'metal, ore)
        consume(agent, 'ore', ore)
        consume(agent, 'food', 1)
        consume(agent, 'tools', 1, 0.1)
    else:
        # Convert up to 2 ore into metal, consume 1 food
        max = query_inventory('ore')
        if max > 2:
            max = 2
        produce(agent, 'metal', max)
        consume(agent, 'ore', max)
        consume(agent, 'food', 1)
else:
    # Fined $2 for being idle
    consume(agent, 'money', 2)
    if not has_food and inventory_is_full():
        make_room_for(agent, 'food', 2)
