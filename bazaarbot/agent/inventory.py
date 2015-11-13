#! /usr/bin/env python


class Inventory(object):
    def __init__(self):
        self.max_size = 0
        self.sizes = {} #key is string value is float
        self.stuff = {} #key is string value is float
        self.ideal = {} #key is string value is float 
    
    def from_data(self, data):
        """data is an InventoryData object"""
        sizes = []
        amounts = []
        for key data.start.keys():
            sizes.append(key)
            amounts.append(data.start[key])
	    self.set_stuff(sizes, amounts)
	    
	    sizes = []
	    amounts = []
	    for key in data.size.keys():
	        sizes.append(key)
	        amounts.append(data.size[key])
	    self.set_sizes(sizes, amounts)
	    
	    sizes = []
	    amounts = []
	    for key in data.ideal.keys():
	        sizes.append(key)
	        amounts.append(data.ideal[key])
	        self.set_ideal(sizes, amounts)
        max_size = data.max_size
    
    def copy(self):
        i = Inventory()
        stufff = []
        stuffi = []
        idealf = []
        ideali = []
        sizesf = []
        sizesi = []
        for key in self.stuff.keys():
            stufff.append(self.stuff[key])
            stuffi.append(key)
        for key in self.ideal.keys():
            idealf.append(self.ideal[key])
            ideali.append(key)
        for key in self.size.keys():
            sizesf.append(self.size[key])
            sizesi.append(key)
        i.set_stuff(stuffi, stufff)
        i.set_ideal(ideali, idealf)
        i.set_sizes(sizesi, sizesf)
        i.max_size = self.max_size
        
        return i
	
	public function destroy():Void
	{
		for (key in _stuff.keys())
		{
			_stuff.remove(key);
		}
		for (key in _ideal.keys())
		{
			_ideal.remove(key);
		}
		for (key in _sizes.keys())
		{
			_sizes.remove(key);
		}
		_stuff = null;
		_ideal = null;
		_sizes = null;
	}
	
	/**
	 * Set amounts of various commodities
	 * @param	stuff_
	 * @param	amounts_
	 */
	
	public function setStuff(stuff:Array<String>, amounts:Array<Float>):Void
	{
		for (i in 0...stuff.length)
		{
			_stuff.set(stuff[i], amounts[i]);
		}
	}
	
	/**
	 * Set how much of each commodity to stockpile
	 * @param	stuff_
	 * @param	amounts_
	 */
	
	public function setIdeal(ideal:Array<String>, amounts:Array<Float>):Void
	{
		for (i in 0...ideal.length)
		{
			_ideal.set(ideal[i], amounts[i]);
		}
	}
	
	public function setSizes(sizes:Array<String>, amounts:Array<Float>):Void
	{
		for (i in 0...sizes.length)
		{
			_sizes.set(sizes[i], amounts[i]);
		}
	}
	
	/**
	 * Returns how much of this
	 * @param	commodity_ string id of commodity
	 * @return
	 */
	
	public function query(good:String):Float
	{
		if (_stuff.exists(good))
		{
			return _stuff.get(good);
		}
		return 0;
	}
	
	public function ideal(good:String):Float
	{
		if (_ideal.exists(good))
		{
			return _ideal.get(good);
		}
		return 0;
	}
	
	public function getEmptySpace():Float
	{
		return maxSize - getUsedSpace();
	}
	
	public function getUsedSpace():Float
	{
		var space_used:Float = 0;
		for (key in _stuff.keys())
		{
			space_used += _stuff.get(key) * _sizes.get(key);
		}
		return space_used;
	}
	
	public function getCapacityFor(good:String):Float
	{
		if (_sizes.exists(good))
		{
			return _sizes.get(good);
		}
		return -1;
	}
	
	/**
	 * Change the amount of the given commodity by delta
	 * @param	commodity_ string id of commodity
	 * @param	delta_ amount added
	 */
	
	public function change(good:String, delta:Float):Void
	{
		var result:Float;
		
		if (_stuff.exists(good))
		{
			var amount:Float = _stuff.get(good);
			result = amount + delta;
		}
		else
		{
			result = delta;
		}
		
		if (result < 0)
		{
			result = 0;
		}
		
		_stuff.set(good, result);
	}
	
	/**
	 * Returns # of units above the desired inventory level, or 0 if @ or below
	 * @param	commodity_ string id of commodity
	 * @return
	 */
	
	public function surplus(good:String):Float
	{
		var amt:Float = query(good);
		var ideal:Float = _ideal.get(good);
		if (amt > ideal)
		{
			return (amt - ideal);
		}
		return 0;
	}
	
	/**
	 * Returns # of units below the desired inventory level, or 0 if @ or above
	 * @param	commodity_
	 * @return
	 */
	
	public function shortage(good:String):Float
	{
		if (!_stuff.exists(good))
		{
			return 0;
		}
		var amt:Float = query(good);
		var ideal:Float = _ideal.get(good);
		if (amt < ideal)
		{
			return (ideal - amt);
		}
		return 0;
	}
	
	//private static var _index:Map<String, Commodity>;
	
	private var _stuff:Map<String, Float>;		// key:commodity_id, val:amount
	private var _ideal:Map<String, Float>;		// ideal counts for each thing
	private var _sizes:Map<String, Float>;		// how much space each thing takes up
}
