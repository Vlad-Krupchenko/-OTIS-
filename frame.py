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
        if self.x>0 and self.y>0 and self.z>0: 
            return 1
        if self.x<0 and self.y>0 and self.z>0:
            return 2
        if self.x<0 and self.y<0 and self.z>0:
            return 3
        if self.x>0 and self.y<0 and self.z>0:
            return 4
        if self.x>0 and self.y>0 and self.z<0:
            return 5
        if self.x<0 and self.y>0 and self.z<0:
            return 6
        if self.x<0 and self.y<0 and self.z<0:
            return 7
        if self.x>0 and self.y<0 and self.z<0:
            return 8
        if  self.x:
        def Dist(self):
        return ((0-self.x)**2+(0-self.y)**2+(0-self.z)**2)**0.5
        