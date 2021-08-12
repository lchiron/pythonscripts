from collections import defaultdict

sums = [2,3,4,5,3]


mydist = defaultdict(list)

for i in range(len(sums)):
    
    for j in range(i+1,len(sums)):
        if sums[j] == sums[i]: 
            mydist[sums[i]].append(j-i)
if mydist == {}:
    print("no")
    exit()
    
for k,v in mydist.items():
    mydist.update({k:min(v)})

minval = min(mydist.values())

print(mydist.items())
for k, v in mydist.items():
    if v == minval:
        print(k)




