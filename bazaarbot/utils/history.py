#! /usr/bin/env python


class History(object):

    def __init__(self):
        self.prices = HistoryLog(Price)
        self.asks = HistoryLog(Ask)
        self.bids = HistoryLog(Bid)
        self.trades = HistoryLog(Trade)
        self.profit = HistoryLog(Profit)
        
    def register(self, good):
        order = [self.prices, self.asks, self.bids, self.trades, self.profit]
        for item in order:
            item.register(good) # not sure if this is going to workd
	
