#RobotName: Malena
from RobotRL import RobotRL

ro=RobotRL()

VALOR_NEGRO = 40
VALOR_DISTANCIA = 100

distD = 0
distI = 0
sensPiso = 0

def Recto():
    ro.setVel(50, 50)

def AvanzarEnNegro(vel):
    sensPiso = ro.getColorPiso()
    if sensPiso <= VALOR_NEGRO:
        ro.setVel(vel,vel)
    else:
        parar()

def Obstaculo():
    distD = ro.getDD()
    distI = ro.getDI()
    result_obst = False;
    if (distD < 50) or (distI < 50):
        result_obst = True

    return  result_obst

def Buscar():
    ro.setVel(10, -70)
    hayObstaculo = Obstaculo()

    if hayObstaculo:
        Empujar()
        ro.esperar(1)

def irDerecha():
    ro.setVel(-50, 0)

def irIzquierda():
    ro.setVel(0, 50)

def girar():
    ro.setVel(60, -60)

def Retroceder():
    ro.setVel(-50, -50)

def Parar():
    ro.setVel(0,0)

def NoCaer():
    if ro.getColorPiso() > VALOR_NEGRO:
        retroceder()
        ro.esperar(1)
        irIzquierda()
        ro.esperar(.5)

def Empujar():
    ro.setVel(100, 100)
    ro.esperar(1)
    ro.setVel(-30, -30)
    ro.esperar(.05)


while ro.step():
    Buscar()





 
