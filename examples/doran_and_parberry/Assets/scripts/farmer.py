#! /usr/bin/env python

wood = query_inventory('wood')
tools = query_inventory('tools')

has_wood = wood >= 1
has_tools = tools >= 1

if has_wood:
    if has_tools:
        # Produce 4 food, consume 1 wood, break tools with 10% chance
        produce(agent, 'food', 4, 1)
        consume(agent, 'wood', 1, 1)
        consume(agent, 'tools', 1, 0.1)
    else:
        # Produce 2 food, consume 1 wood
        produce(agent, 'food', 2, 1)
        consume(agent, 'wood', 1, 1)
else:
    # Fined $2 for being idle
    consume(agent, 'money', 2)
