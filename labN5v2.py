import math 

def j(x1,y1, x2,y2):
    return math.sqrt ((x2-x1)**2+(y1-y2)**2)
    
ax=float (input("Надо кординаты , введите сюда" ))   
ay=float (input("Надо кординаты , введите сюда "))    
bx=float (input("Надо кординаты , введите сюда "))
By=float (input("Надо кординаты , введите сюда "))
Cx=float (input("Надо кординаты , введите сюда "))
Cy=float (input("Надо кординаты , введите сюда "))

h=j(ax, ay, 0,0)
k=j(bx, By , 0 , 0)
l=j(Cx, Cy, 0 ,0)
if h<=k and h<=l:
    print ("a")

elif k<=h and  k<=l:
    print("b")

elif l<=k and l<=h:
    print("c")