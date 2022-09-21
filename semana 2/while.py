from ssl import CERT_NONE


def run():
    pass
    
    num_user = int(input("Ingresa el numero  hasta el cual quiere llegar "))

    cnt = 0
    ptn = 1+cnt
    while ptn < num_user:
        print('El numero se esta repitiendo... ' +str(cnt)
        + ' Estamos alcanzando tu resultado esperado ' + str(ptn))
        cnt += 1
        ptn = 1+cnt 

if __name__ == '__main__':
    run()



#Repetir un número dado por el usuario las veces lo indique el usuario