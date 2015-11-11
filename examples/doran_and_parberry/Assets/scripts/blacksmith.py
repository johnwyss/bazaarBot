#! /usr/bin/env python


food = query_inventory('food')
metal = query_inventory('metal')

has_food = food >= 1
has_metal = metal >= 1

if has_food and has_metal:
    # Convert all metal into tools
    produce(agent, 'tools', metal)
    consume(agent, 'metals', metal)
else:
    # Fined $2 for being idle
    consume(agent, 'money', 2)
    if not has_food and inventory_is_full():
        make_room_for(agent, 'food', 2)
