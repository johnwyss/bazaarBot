#! /usr/bin/env python

food = query_inventory('food')
tools = query_inventory('tools')

has_food = food >= 1
has_tools = tools >= 1

if has_food:
    if has_tools:
        # Produce 2 wood, consume 1 food, break tools with 10% chance
        produce(agent, 'wood', 2)
        consume(agent, 'food', 1)
        consume(agent, 'tools', 1, 0.1)
    else:
        # Produce 1 wood, consume 1 food
        produce(agent, 'wood', 1)
        consume(agent, 'food', 1)
else:
    # Fined $2 for being idle
    consume(agent, 'money', 2)
    if not has_food and inventory_is_full():
        make_room_for(agent, 'food', 2)
