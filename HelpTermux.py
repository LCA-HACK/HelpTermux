import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'

os.system("clear")

def baner():

        print(RED+"| |     _____   ____")
        print(RED+"| |    | ___|  | __ |")
        print(RED+"| |    | |     ||__||")
        print(RED+"| |__  | |__   ||  ||")
        print(RED+"|____| |___|   ||  ||")
baner()

print("\nCreado por L.C.A HACK")

while True:
        print(YELLOW+"[1] Instalar paquetes basicos")
        print("\n[2] Actualizar Termux")
        print("\n[3] Dar permisos de  almacenamiento a termux")
        print("\n[4] Salir")
        opcion=input("\nElije una opcion: ")
        if opcion=="1":
                os.system("pkg install -y git; pkg install -y python; pkg install -y python2; pkg install -y php; pkg install -y openssh; pkg  install -y wget; pkg install -y vim;")
        if opcion=="2":
                os.system("clear")
                print(GREEN+"En la primera ventana que aparezca debes\nseleccionar todas las opciones y despues dar en ok\nEn la segunda ventana solo pones la tercera opcion y das en ok.")
        if opcion=="3":
                os.system("clear")
                os.system("termux-setup-storage")
        break
