from frame import *
import random
j=[]
for i in range(100):
    j.append(PointSpace(random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)))
for i in j:
    if i.Octant() in [1,3]:
        i.DisplayCoord()
