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

    def generate_offers(self, bazaar, good)
	
	public function generateOffers(bazaar:Market, good:String):Void
	{
		//no implemenation -- provide your own in a subclass
	}
	
	public function updatePriceModel(bazaar:Market, act:String, good:String, success:Bool, unitPrice:Float = 0):Void
	{
		//no implementation -- provide your own in a subclass
	}
	
	public function createBid(bazaar:Market, good:String, limit:Float):Offer
	{
		//no implementation -- provide your own in a subclass
		return null;
	}
	
	public function createAsk(bazaar:Market, commodity_:String, limit_:Float):Offer
	{
		//no implementation -- provide your own in a subclass
		return null;
	}
	
	public function queryInventory(good:String):Float
	{
		return _inventory.query(good);
	}
	
	public function changeInventory(good:String, delta:Float):Void
	{
		_inventory.change(good, delta);
	}
	
	/********PRIVATE************/
	
	private var _logic:Logic;
	private var _inventory:Inventory;
	private var _priceBeliefs:Map<String, Point>;
	private var _observedTradingRange:Map<String, Array<Float>>;
	private var _profit:Float = 0;	//profit from last round
	private var _lookback:Int = 15;
	
	private function get_inventorySpace():Float
	{
		return _inventory.getEmptySpace();
	}
	
	public function get_inventoryFull():Bool
	{
		return _inventory.getEmptySpace() == 0;
	}
	
	private function get_profit():Float
	{
		return money - moneyLastRound;
	}
	
	private function determinePriceOf(commodity_:String):Float
	{
		var belief:Point = _priceBeliefs.get(commodity_);
		return Quick.randomRange(belief.x, belief.y);
	}
	
	private function determineSaleQuantity(bazaar:Market, commodity_:String):Float
	{
		var mean:Float = bazaar.getAverageHistoricalPrice(commodity_,_lookback);
		var trading_range:Point = observeTradingRange(commodity_);
		if (trading_range != null)
		{
			var favorability:Float = Quick.positionInRange(mean, trading_range.x, trading_range.y);
			//position_in_range: high means price is at a high point
			
			var amount_to_sell:Float = Math.round(favorability * _inventory.surplus(commodity_));
			if (amount_to_sell < 1)
			{
				amount_to_sell = 1;
			}
			return amount_to_sell;
		}
		return 0;
	}
	
	private function determinePurchaseQuantity(bazaar:Market, commodity_:String):Float
	{
		var mean:Float = bazaar.getAverageHistoricalPrice(commodity_,_lookback);
		var trading_range:Point = observeTradingRange(commodity_);
		if (trading_range != null)
		{
			var favorability:Float = Quick.positionInRange(mean, trading_range.x, trading_range.y);
			favorability = 1 - favorability;			
			//do 1 - favorability to see how close we are to the low end
			
			var amount_to_buy:Float = Math.round(favorability * _inventory.shortage(commodity_));
			if (amount_to_buy < 1)
			{
				amount_to_buy = 1;
			}
			return amount_to_buy;
		}
		return 0;
	}
		
	private function getPriceBelief(good:String):Point
	{
		return _priceBeliefs.get(good);
	}
	
	private function observeTradingRange(good:String):Point
	{
		var a:Array<Float> = _observedTradingRange.get(good);
		var pt:Point = new Point(Quick.minArr(a), Quick.maxArr(a));
		return pt;
	}
}


