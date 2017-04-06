import random

fullness = random.randint(0,2)
            
if fullness == 0:
    range_min = 0
    range_max = 14
if fullness == 1:
    range_min = 16
    range_max = 29
if fullness == 2:
    range_min = 30
    range_max = 45
    
print("fullness=",fullness,"rangemin=",range_min,"rangemax=",range_max)

for i in range (0,9):
    rand = random.randint(range_min, range_max)
    PercFull = (45 - rand) / 45
    
    if (PercFull < 1/3):
        res= 0
    elif (PercFull < 2/3 and PercFull > 1/3):
        res= 1
    else:
        res= 2
    
    print("rand=",rand,"res=",res)