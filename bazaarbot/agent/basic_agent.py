#! /usr/bin/env python


from inventory import *
from econ_nount import *
from quick import *
from inventory_data import *
from logic import *


class AgentData(object):
	""" This is the structure for holding data for new agents"""
	def __init__(self, class_name, money, inventory, logic_name, logic, lookback=None):
		"""
		class_name: string
		money: float
		inventory: InventoryData object
		logic_name: String
		logic: Logic object
		lookback: int
		"""
		self.class_name = class_name
		self.money = money
		self.inventory = inventory
		self.logic_name = logic_name
		self.logic = logic
		self.lookback = lookback


class BasicAgent(object):
    def __init__(self, d, data):
	    """ id: int, data: AgentData object"""
	    self.id = id #must be a unique integer identifier # TODO: make this be unique in class
	    self.class_name = data.class_name #string identifier, 'farmer', 'woodcutter', etc
        self.money = data.money
        self.inventory = Inventory()
        self.inventory.from_data(data.inventory) #not sure what this does yet... some sort of inititializing?
        self.logic = data.logic
        if not data.lookback:
            self.lookback = 15
        else:
            self.lookback = data.lookback
        self.price_beliefs = {} #key is string with commodity, value is an x,y point or tuple of points... play with this
        self.observed_trading_range = {} # key is string, value is list of floats
        self.destroyed = False
        
        	
	public var moneyLastRound(default, null):Float;
	public var profit(get, null):Float;
	public var inventorySpace(get, null):Float;
	public var inventoryFull(get, null):Bool;
	
		private var _logic:Logic;
	private var _inventory:Inventory;
	private var _priceBeliefs:Map<String, Point>;
	private var _observedTradingRange:Map<String, Array<Float>>;
	private var _profit:Float = 0;	//profit from last round
	private var _lookback:Int = 15;
	
        
        
    def destroy(self):
        self.destroyed = True
        self.inventory.destroy()
        # not sure this is needed in python... have to see later
        for key in self.price_beliefs:
            del self.price_beliefs[key]
        for key in self.observed_trading_range:
            del self.observed_trading_range[key]
        self.price_beliefs = None
        self.observed_trading_range = None
        self.logic = None

   def init(self, market):
       """takes a Market object"""
        list_goods = market.get_goods_unsafe()
        for item in list_goods:
            trades = []
            price = market.get_average_historical_price(item, self.lookback)
            trades.append(price * 0.5)
            trades.append(price * 1.5) #append two fake trades to generate a range
            # Set initial price belief and observed trading range
            self.observed_trading_range[item] = trades
            self.price_beliefs[item] = Point(price * 0.5, price * 1.5) #Points could just be tuples not sure they need anything else
    
    def simulate(self, market):
        """takes a Market object"""
        self.logic.perform(self, market)

    def generate_offers(self, bazaar, good):
        """bazaar is Market object, good is String describing good"""
        pass # implement in subclass
    
    def update_price_model(self, bazaar, act, good, success, unit_price=0.0):
        """bazaar: Market object, act: String, good: String, succes: Bool, unit_price: Float"""
        pass # implement in sublclass
    
    def create_bid(self, bazaar, good, limit):
        """bazaar: Market, good:String, limit:Float"""
        pass # implement in sublcass
    
    def create_ask(self, bazaar, commodity, limit):
        """bazaar: Market, commodity:String, limit:Float"""
        pass # implement in sublcass

    def query_inventory(self, good):
        return self.inventory.query(good)
        
    def change_inventory(self, good, delta):
        self.inventory.change(good, delta)
	
    @property
    def get_inventory_space(self):
        return self.inventory.get_empty_space()
        
    @property
    def get_inventory_full(self):
        return self.inventory.get_empty_space() == 0
	
    @property
    def get_profit(self):
        return self.money - self.money_last_round
	
    def determin_price_of(self, commodity):
        belief = self.price_beliefs[commodity]
        return random.randint(belief.x, belief.y) 
        #original line: Quick.randomRange(belief.x, belief.y);
	
   def determine_sale_quantity(self, bazaar, commodity):
        mean = bazaar.get_average_historical_price(commodity, self.lookback)
        trading_range = self.observe_trading_range(commodity) # returns a Point object
       	
        if trading_range:
       	    # TODO:  Not sure exactly what this does... this needs to be changed
       	    favorability = Quick.position_in_range(mean, trading_range.x, trading_range.y) 
       	    # position_in_range: high means price is at a high point
       	    
            amount_to_sell = round(favorability * self.inventory.surplus(commodity))
            if ammount_to_sell < 1:
                ammount_to_sell = 1
            return amount_to_sell
    
    def determine_purchase_quantity(self, bazaar, commodity):
        mean = bazaar.get_average_historical_price(commodity, self.lookback)
        trading_range = self.observe_trading_range(commodity)
        
        if trading_range:	
            # TODO:  Not sure exactly what this does... this needs to be changed
       	    favorability = Quick.position_in_range(mean, trading_range.x, trading_range.y) 
       	    favorability = 1 - favorability #1 - favorability to see how close we are to the low end
            
            amount_to_buy = round(favorability * self.inventory.shortage(commodity))
            if amount_to_buy < 1:
                amount_to_buy = 1
            return amount_to_buy
	
	@property
	def get_price_belief(self, good):
	    return self.price_beliefs[good]
		
    def observe_trading_range(self, good):
        a = self.observed_trading_range[good]
        # TODO: this needs fixed not sure what it does
        return Point(Quick.minArr(a), Quick.maxArr(a))


