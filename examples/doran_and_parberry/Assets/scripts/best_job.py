#! /usr/bin/env python

def best_job(commodity):
    jobs = {'food': 'farmer', 'wood': 'woodcutter', 'ore': 'miner', 'metal': 'refiner', 'tools': 'blacksmith'}
    return jobs[commodity]
