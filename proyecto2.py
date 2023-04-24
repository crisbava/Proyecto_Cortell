from os import system; system("cls"); import time; 

inventario={1:["lucky", 100000, 50], 2:["Belmont", 900000, 25], 3:["Marboro",85000,35], 4:["Belmont blanco",88000,400], 5:["lucky azul",96000], 6:["foresta",70000,300]}
clientes = {1065875449:"Didier guerrero"}


#FUNCIONES -> DONDE VEA COSAS REPETIDAS

#ADMINISTRADOR

#GESTIONE CLIENTES

#EXCEPCIONES

precios={100000,90000,85000,96000,88000,70000}
cont_ventas=0
cont_plata=0
dinero_total=[]
cantidad_decenas=0
numero_identificacion=[]
nombre_clientes=[clientes]
cont_clientes=0
facturas=[nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total]

def iniciar():
    print("Ha iniciado sesion")
    print("1. Administrador")
    print("2. empleado")
    opcion=input("eliga una opcion : ")
    while True:
            if opcion==1:
                administrador(inventario)
            elif opcion==2:
                trabajador()
            else:
                print("La opcion no es valida")
                print(""); input("Pulse enter para continuar"); system("cls")
            return iniciar



def trabajador():
    print("minorista")
    print("mayorista")
    usuario=input("Ingrese su nombre de usuario: ")
    contraseña=(input("ingrese su contraseña: ")); system("cls")
    if usuario == "minorista" and contraseña == 123:
        datos_clientes(cont_clientes,nombre_clientes,numero_identificacion,clientes)
        menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas); time.sleep(1)
        print(factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total))
        factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total)
        system("cls"); print("Saliendo de sesión...")
    elif usuario == "mayorista" and contraseña == 1234:
        datos_clientes(cont_clientes,nombre_clientes,numero_identificacion,clientes)
        menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas); time.sleep(1)
        factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total)
        system("cls"); print("Saliendo de sesión...")
    else:
        print("Error, intentalo de nuevo"); print("")
        input("Pulse enter para continuar"); system("cls")
    return
def datos_clientes(cont_clientes,nombre_clientes,numero_identificacion,clientes):
    nombre_clientes=(input("escriba nombre completo y apellidos: "))
    numero_identificacion=(input("ingrese el numero de identificacion: "))
    cont_clientes+=1
    return
def administrador(inventario):
    usuario=input("Ingrese su nombre de usuario: ")
    contraseña=(input("ingrese su contraseña: ")); system("cls")
    if usuario == "minorista" and contraseña == 123:
        print("Menu principal")
        print("1. Desea anexar un producto nuevo o cambiar precio")
        print("2. Eliminar un producto de la lista")
        print("3. Desea volver al nenu iniciar")
        opcion=int(input("Seleccione una opción: ")); system("cls")
        if opcion==1:
            print(inventario)
            x=(int(input("Desea anexar un producto nuevo o cambiar precio: ")))
            posicion=inventario.update(x)
            print(posicion)
        elif opcion==2:
            print(inventario)
            x=(int(input("ingrese el elemento que desea el dato a borrar: ")))
            posicion=inventario.update(x)
            print(posicion)
        elif opcion==3:
            print(""); print("volveras al menu principal"); iniciar()
        else:
            return usuario
    else:
        print(""); print("volveras al menu principal"); iniciar()

def menu_principal():
    print("Bienvenido a la venta del cigarrillo"); print("")
    print("1. lucky verde")
    print("2. belmont")
    print("3. marboro rojo")
    print("4. belmont blanco")
    print("5. lucky azul")
    print("6. foresta")
    print("7. imprimir factura"); print("")
    return
def menu_segundario():
                print("cuantas decenas deseas comprar"); print("")
                print("1. 1 decena")
                print("2. 2 decena")
                print("3. 3 decena")
                print("4. 4 decena")
                print("5. 5 decena en adelante")
                print("6. por caja")
                print("7. desea salir al menu principal")
                return menucliente_mayorista

def menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas):
    menu_principal
    opcion=int(input("Seleccione una opción: ")); system("cls")
    if opcion == 1:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==100000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 2:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==90000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 3:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==85000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 4:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==96000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 5:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==88000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 6:
        if precios:
            cont_plata=int(input("ingrese el valor a pagar: "))
            if cont_plata==100000:
                print(""); input("Pulse enter para continuar"); menucliente_minorista(dinero_total,inventario,precios,cont_ventas,cont_plata)
        else:
            print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
            print(""); input("Pulse enter para continuar"); system("cls")
    elif opcion == 7:
        print("el total a pagar es:"); factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total)
    else:
        print("Error, intentalo de nuevo"); print("")
    return
def menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas):
    menu_principal
    opcion=int(input("Seleccione una opción: ")); system("cls")
    while True:
            if opcion == 1:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=100000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=100000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=100000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=100000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=100000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=5000000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 7:
                    print("La empresa de cigarrillo a cerrado"); print("")
                    menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return
            if opcion == 2:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=90000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=90000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=90000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=90000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=90000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=4500000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 7:
                    print("La empresa de cigarrillo a cerrado"); print("")
                    menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return
            if opcion == 3:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=85000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=85000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=85000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=85000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=85000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=4250000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 7:
                    print("La empresa de cigarrillo a cerrado"); print("")
                    menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return
            if opcion == 4:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=96000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=96000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=96000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=96000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=96000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=4800000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 7:
                    print("La empresa de cigarrillo a cerrado"); print("")
                    menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return
            if opcion == 5:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=88000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=88000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=88000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=88000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=88000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=4400000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 7:
                    print("La empresa de cigarrillo a cerrado"); print("")
                    menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return
            if opcion == 6:
                menu_segundario()
                opcion=int(input("Seleccione una opción: ")); system("cls")
                if opcion==1:
                    if precios:
                        cont_plata=70000
                        cantidad_decenas+=1
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion==2:
                    if precios:
                        cont_plata=70000*2
                        cantidad_decenas+=2
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 3:
                    if precios:
                        cont_plata=70000*3
                        cantidad_decenas+=3
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 4:
                    if precios:
                        cont_plata=70000*4
                        cantidad_decenas+=4
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 5:
                    if precios:
                        x=int(input("digite cuanta decenas necesita: "))
                        cont_plata=70000*x
                        cantidad_decenas+=x
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                elif opcion == 6:
                    if precios:
                        x=int(input("digite cuanta cajas necesitas necesita: "))
                        cont_plata=3500000*x
                        cantidad_decenas+=x*50
                        dinero_total=cont_plata
                        print(f"su valor a cancela es",dinero_total,"pesos")
                        print(""); input("Pulse enter para continuar"); menucliente_mayorista(dinero_total,inventario,precios,cont_ventas,cont_plata,cantidad_decenas)
                    else:
                        print("No se ha realizado ninguna venta hoy, porque no cumple con el precio establecido del producto")
                        print(""); input("Pulse enter para continuar"); system("cls")
                
                elif opcion == 7:
                    print("el total a pagar es:"); factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total)
                else:
                    print("Error, intentalo de nuevo"); print("")
                return

def factura(nombre_clientes,numero_identificacion,cantidad_decenas,dinero_total):
    print("nombre del cliente:",nombre_clientes)
    print("numero de identificacion:",numero_identificacion)
    print("cantidad de decenas:",cantidad_decenas)
    print("total a pagar es:",dinero_total)




print("ha iniciado sesion en la empresa un respiro mas")
iniciar()



