#!/usr/bin/env python3

"""#print the proto list
proto = ["ssh", "http", "https"]
print(proto)

#print the second item in the proto list
print(proto[1])

#extend the list with a d, n, s
proto.extend("dns") # this line will add d, n, and s
print(proto)"""

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# Print to find what index position 80 is at in proto and then print that.

inde = proto.index(80, 0)
print(f'port 80 is in the {inde} index spot on list proto.')
#set num var
num = 0
#for loop for list proto
for selected in proto:
    print(selected)
    selected = list(selected)
    num = selected.count('s') + num
#print the number of S's
print(f'There are {num} s')
