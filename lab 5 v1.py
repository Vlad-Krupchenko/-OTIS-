import math 

def j (x):
    if x >0.53:
        return 3 - 0.127*x + math.log(math.fabs(x+2), math.e)

    elif -1.2 < x  <= 0.53:
        return  2.35*math.e **(4*x-1) + math.cos (x) 
        
    else:
        return 0.11 * math.sqrt (x+0.3 * math.cos(x))

x= float (input ("Введи числа , дружище  ") ) 

print (j(x))