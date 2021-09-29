import collections
#Creating default dict to store cities connection
gr1=collections.defaultdict(list)

#Read input file from the source location
with open('/Users/saketh/PycharmProjects/Broadridge-Coding-Assessment/Cities.txt', "r") as data_file:
    for line in data_file:
        source,dest=line.rstrip().split(",")
        gr1[source].append(dest)
        gr1[dest].append(source)
#Total number of cities
N=len(gr1)
#s = start
#d = Destination
def isReachable(s, d):
    for x in gr1[s]:
        if x==d:
            return True
        for j in gr1[x]:
            if j==d:
                return True
    return False

# Test Case 1
# Adding Entries for the start city and destination to check the connection:

u = 'Seattle';#starting city
v = 'Boston'#destination city

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 2
u = 'Tampa';
v = 'St.Petersburg'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 3
u = 'Kansas';
v = 'Houston'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 4
u = 'Boston';
v = 'Hartford'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 5
u = 'Boston';
v = 'Tampa'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 6
u = 'Philadelphia';
v = 'Seattle'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))

#Test case 7
u = 'Boston';
v = 'Austin'

if isReachable(u, v):
    print("Cities - %s , %s are connected" % (u, v))
else:
    print("Cities - %s , %s are not connected" % (u, v))