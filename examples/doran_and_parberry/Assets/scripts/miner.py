#! /usr/bin/env python

food = query_inventory('food')
tools = query_inventory('tools')

has_food = food >= 1
has_tools = tools >= 1

if has_food:
    if has_tools:
        # Produce 4 ore, consume 1 food, break tools with 10% chance
        produce(agent, 'ore', 4)
        consume(agent, 'food', 1)
        consume(agent, 'tools', 1, 0.1)
    else:
        # Produce 2 ore, consume 1 food
        procude(agent, 'ore', 2)
        consume(agent, 'food', 1)
else:
    # Fined $2 for being idle
    consume(agent, 'money', 2)
    if not has_food and inventory_is_full():
        make_room_for(agent, 'food', 2)
