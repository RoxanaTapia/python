import fake_database

CACHE = {}

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
	pass
            

def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    if any(CACHE):

    	c = len(CACHE.keys())

		for x in range(c,0,-1):
			if c - x < 5:
				print dicti.items()[x-1]      
    	
    	'''
    	for i in range(0, 5):
    		if i >= len(CACHE.keys()):
    			print "Empty"
    		else:
    			print CACHE.items()[i]

    	'''
    	#print CACHE
    else:
    	print "Cache is empty."


def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    """
    key = a,b
    result = fake_database.russian(a,b)
    CACHE[key] = result
    print result
