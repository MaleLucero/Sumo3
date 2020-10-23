#RobotName: Hitoshi
from RobotRL import RobotRL

ro=RobotRL()

#-----variables------#
def retroceder():
    ro.setVel(-40, -40)

def girarD():
    ro.setVel(-20, 20)

def girarI():
    ro.setVel(20, -20)

def NoCaer():
    if ro.getColorPiso()>85:
      ro.setVel(0, 0)
      ro.esperar(0.2)
      girarD()
      ro.esperar(1.5)

def Buscar():
    IZ=ro.getDI()
    DER=ro.getDD()
    ro.setVel(50, 20)
    if (IZ<100 or DER<100):
        Atacar()
        ro.esperar(0.2)
        return

def Adelante():
    ro.setVel(40, 40)

def Atacar():
    ro.setVel(100, 100)

#-----MainLoop------#
while ro.step():
    Buscar()
    ro.esperar(0.2)
    NoCaer()

