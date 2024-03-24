import math
bom = open("BoM Test.txt", "r")
conf = dict()

for line in bom:
    #Store number of possible chairs & production group
    x = float(line.split()[3]) / float(line.split()[2])
    y = line.split()[0]
    #Create unique values for production groups
    if y not in conf:
        conf[y] = list()
        conf[y].append(line.split()[1])
        conf[y].append(math.floor(x))
    #Check for the most available option per production group    
    elif x > conf[line.split()[0]][1]:
        conf[y][0] = (line.split()[1])
        conf[y][1] = (math.floor(x)) 
#Determine the least available component of the configuration    
minqty = None
for line in conf:
    if minqty == None or conf[line][1] < minqty:
        minqty = conf[line][1]
#Share results of analysis
print("You can produce", minqty, "chairs by following this configuration:")
for line in conf:
    print(line, conf[line][0])