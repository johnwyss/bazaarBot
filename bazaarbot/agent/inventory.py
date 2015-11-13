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
	
	def destroy(self) # not sure if this is actually needed
	    for key in self.stuff.keys():
	        del self.stuff[key]
	    for key in self.ideal.keys():
	        del self.ideal[key]
	    for key in self.sizes.keys():
	        del self.sizes[key]
	    self.stuff = None
	    self.ideal = None
	    self.sizes = None
	

    # set ammounts for various commodities
    def set_stuff(self, stuff, amounts):
        """stuff: list of strings, amounts: list of floats"""
        # TODO: use zip here
        for s, a in zip(stuff, amounts):
            self.stuff[s] = a

	# set how much of each commidty to stockpile
	def set_ideal(self, ideal, amounts):
	    """ideal: list of strings, amounts: list of floats"""
	    for i, a in zip(ideal, amounts):
	        self.ideal[i] = a
	        
   def set_sizes(self, sizes, amounts):
       """sizes: list of strings, amounts list of floats"""
       for s, a in zip(sizes, amounts):
           self.sizes[s] = a
	
    # return amount of good
    def query(self, good):
        if self.stuff.get(good, False):
            return self.stuff[good] 
            # At first I thought not needed, but this makes sure you can get goods that might not exist
   
    def ideal(self, good):
        if self.ideal.get(good, False):
            return self.ideal[good]
            
    def get_empty_space(self):
        return self.max_size - self.get_used_space()
	
    def get_used_space(self):
        space_used = 0
        for key in self.stuff.keys():
            space_used += self.stuff[key] * self.sizes[key]
		return space_used
	
	def get_capacity_for(self, good):
	    if self.sizes.get(good, False):
	        return self.sizes[good]
	    else:
	        return -1
    
    #change the amount of the given commodity by delta	 
	def change(self, good, delta):
	    result = 0.0
	    if self.stuff.get(good, False):
	        amount = self.stuff[good]
	        result = amount + delta
	    else:
	        result = delta
	    if result < 0:
	        result = 0
        self.stuff[good] = result
	
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
