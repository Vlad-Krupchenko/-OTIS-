class PointSpace:
    def  __init__(self, x ,y ,z) -> None:
        self.x=x
        self.y=y
        self.z=z
    def  setcord(self, x ,y ,z) -> None:
        self.x=x
        self.y=y
        self.z=z
    def DisplayCoord (self):
        print(f"x={self.x} y={self.y} z={self.z}")
    def Octant(self):
        if x>0 and y>0: 
            return 1
        if x>0 and y<0:
            return 2
        if x<0 and y<0:
            return 3
        if x>0 and y<0:
            return 4
        
    def Dist(self):
        return ((0-self.x)**2+(0-self.y)**2+(0-self.z)**2)**0.5
        