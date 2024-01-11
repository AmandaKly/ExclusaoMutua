import time
import threading
import random

def start(func):
    thread = threading.Thread(target=func)
    thread.start()

lista=[]
Recurso = False
print('O Recurso está desocupada ..')


def fila():
    global Recurso
    Recurso = True
    print(f"o usuário {lista[0]} está usando o Recurso.")
    time.sleep(5)
    Recurso = False
    print(f"Usuário {lista[0]} liberou o Recurso ...\n\n")
    lista.pop(0)
    time.sleep(4)
    print(f"usuário {lista[0]} pode usar o Recurso. \n")
    time.sleep(5)

espera = 1 


while True:
    
    if Recurso != True :
        time.sleep(7)
        num=1
        while num<4:
            id = random.randint(1, 100)
            lista.append(id)
            num+=1
        print(f"Recurso liberado para o usuário {lista[0]}. . .")
        start(fila)
        
        time.sleep(2)
        espera = 1
    elif espera == 1:
        
        print(f"Próximo da lista {lista[1]}. \n")
        print(f"Fila de espera {lista}. \n")
        espera=2

