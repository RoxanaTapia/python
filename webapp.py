"""
Simulation of Web App Architecture

Service: The Russian Peasant's Algorithm

Architecture Include:

 - App Computer (Modules)
 - Database (--) --> Russian Peasant Algorithm
 - Load Balancer (Algorithm)

+-----+   +-----+   +-----+
| APP |   | APP |   | APP |
|  1  |   |  2  |   |  3  |
+-----+   +-----+   +-----+
"""


## How does a load balancer work?

## 1)   Random
## 2)   Looping
## 3)   Load Based

## Server names
SERVERS = ['APP1', 'APP2', 'APP3']

lastServer = 0

def get_server():
	"""
	Your code in this function.
	No Inputs
	Output: Print the server name
	"""

	global lastServer

	if len(SERVERS) != 0:
		if lastServer >= len(SERVERS):
			lastServer = 0
			get_server()
		else:
			print SERVERS[lastServer]
			lastServer+=1

## Testing the function
if __name__ == '__main__':
	for i in range(8):
		get_server()

## APP1
## APP2
## APP3
## APP1
## APP2
## APP3
## APP1
## APP2
## APP3

'''
#TESTS
1. Requested output archieved
2. It works with a larger amount of servers (and servers number is less than the number of requests)
3. It wotks for a larger number of servers than requests
4. It works for a equal number of servers and requests

5. It works with 1 server (all requests are processed through the same server)
6.* It fails with no servers:
		x RuntimeError: maximum recursion depth exceeded
		- Solved not processing the requests



'''