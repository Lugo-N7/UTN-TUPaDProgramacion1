print("\nMenu de ejercicios:")
print("(1) Ejercicio 1")
print("(2) Ejercicio 2")
print("(3) Ejercicio 3")
print("(4) Ejercicio 4")
print("(5) Ejercicio 5")

opcion_tp = input("Opcion: ")
while not opcion_tp.isdigit() or int(opcion_tp) not in (1, 2, 3, 4, 5):
    if not opcion_tp.isdigit():
        print("Error: ingrese un número válido.")
    elif int(opcion_tp) not in (1, 2, 3, 4, 5):
        print("Error: opción fuera de rango.")
    opcion_tp = input("Opcion: ")

opcion_tp = int(opcion_tp)

if opcion_tp == 1: # Ejercicio 1
    
    total_con_descuento = 0
    total_sin_descuento = 0
    nombre = input("Ingrese el nombre: ")
    while not nombre.isalpha():
        print("Solo se permite ingresar letras: ")
        nombre = input("Ingrese el nombre: ")

    cantidad = input("Ingrese la cantidad: ")
    while not cantidad.isdigit() or int(cantidad) == 0: 
        print("Ingrese solo numeros mayores que cero: ")
        cantidad = input("Ingrese la cantidad: ")
    cantidad = int(cantidad)

    for i in range (1, cantidad + 1):
        precio = input(f"Ingrese el precio del articulo {i}: ")
        while not precio.isdigit() or int(precio) == 0: 
            print("Ingrese solo numeros mayores que cero: ")
            precio = input("Ingrese el precio: ")
        precio = int(precio)
        descuento = input("Posee descuento (S/N): ").lower()
        while descuento not in ("n", "s"):
            descuento = input("Posee descuento (S/N): ").lower()
        if descuento == "s":
            total_con_descuento += precio * 0.9
        else: 
            total_con_descuento += precio
        total_sin_descuento += precio

    print(f"\nCliente: {nombre.title()}")
    print(f"Cantidad de productos: {cantidad}")
    print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
    print(f"Total con descuentos: ${total_con_descuento:.2f}")
    print(f"Ahorro: ${total_sin_descuento - total_con_descuento:.2f}")
    print(f"Promedio por producto: ${total_con_descuento/cantidad:.2f}")

elif opcion_tp == 2:  # Ejercicio 2
   
    intento = 1
    menu = 0
    while intento <= 3:
        usuario = input(f"Intento {intento}/3 - Usuario: ")
        clave = input("Clave: ")
        if usuario == "alumno" and clave == "python123":
            print("Acceso concedido!\n")
            break   
        else:
            intento += 1
            if intento != 3:
                print("Error: credenciales inválidas.\n")
            
    if intento > 3:
        print ("\nCUENTA BLOQUEADA")
        exit()

    while menu != 4:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir\n")
        opcion = input("Opcion: ")

        while not opcion.isdigit() or int(opcion) not in (1, 2, 3, 4):
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            elif int(opcion) not in (1, 2, 3, 4):
                print("Error: opción fuera de rango.")
            opcion = input("Opcion: ")

        opcion = int(opcion)
        if opcion == 1:
            print("Inscripto\n")
        elif opcion == 2:
            clave = input("Nueva clave: ") 
            while len(clave) < 6:
                print("Error: mínimo 6 caracteres.")
                clave = input("Nueva clave:  ") 
            print("Se ha cambiado la clave!")
        elif opcion == 3:
            print("\nTu esfuerzo de hoy es el éxito de mañana\n")
        else:
            break

elif opcion_tp == 3:  # Ejercicio 3

   
    opcion = 0
    lunes_vacio = 0
    martes_vacio = 0
    lunes = 0
    martes = 0
    lunes1 = lunes2 = lunes3 = lunes4 = ""
    martes1 = martes2 = martes3 = ""

    operador = input("Ingrese nombre del operador: ")
    while not operador.isalpha():
        print("Solo se permite ingresar letras: ")
        operador = input("Ingrese nombre del operador: ")
    while opcion != 5:
        print("Menu:")
        print("(1) Reservar turno")
        print("(2) Cancelar Turno")
        print("(3) Ver agenda del dia")
        print("(4) Ver resumen general")
        print("(5) Cerrar sistema")
        opcion = input("Opcion: ")
        while not opcion.isdigit() or int(opcion) not in (1, 2, 3, 4, 5):
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            elif int(opcion) not in (1, 2, 3, 4, 5):
                print("Error: opción fuera de rango.")
            opcion = input("Opcion: ")

        opcion = int(opcion)

        if opcion == 1:
            print("Elegir dia (1) Lunes (2) Martes: ")
            dia = input("Dia: ")
            while not dia.isdigit() or int(dia) not in (1, 2):
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                elif int(dia) not in (1, 2):
                    print("Error: opción fuera de rango.")
                dia = input("Dia: ")

            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
            while not nombre_paciente.isalpha():
                print("Solo se permite ingresar letras: ")
                nombre_paciente = input("Ingrese el nombre: ").lower()
        
            if int(dia) == 1:
                if nombre_paciente in (lunes1, lunes2, lunes3, lunes4):
                    print("El paciente ya posee un turno el dia lunes")
                else:
                    if lunes1 == (""):
                        lunes1 = nombre_paciente
                        print("1º Turno asignado del dia Lunes")
                    elif lunes2 == (""):
                        lunes2 = nombre_paciente
                        print("2º Turno asignado del dia Lunes")
                    elif lunes3 == (""):
                        lunes3 = nombre_paciente   
                        print("3º Turno asignado del dia Lunes") 
                    elif lunes4 == (""):
                        lunes4 = nombre_paciente
                        print("4º Turno asignado del dia Lunes")

            if int(dia) == 2:
                if nombre_paciente in (martes1, martes2, martes3):
                    print("El paciente ya posee un turno el dia martes")    
                else:
                    if martes1 == (""):
                        martes1 = nombre_paciente
                        print("1º Turno asignado del dia Martes")
                    elif martes2 == (""):
                        martes2 = nombre_paciente
                        print("2º Turno asignado del dia Martes")
                    elif martes3 == (""):
                        martes3 = nombre_paciente   
                        print("3º Turno asignado del dia Martes") 

            
        elif opcion == 2:
            print("Elegir dia (1) Lunes (2) Martes: ")
            dia = input("Dia: ")
            while not dia.isdigit() or int(dia) not in (1, 2):
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                elif int(dia) not in (1, 2):
                    print("Error: opción fuera de rango.")
                dia = input("Dia: ")  

            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
            while not nombre_paciente.isalpha():
                print("Solo se permite ingresar letras: ")
                nombre_paciente = input("Ingrese el nombre: ").lower()

            if int(dia) == 1:
                if lunes1 == nombre_paciente:
                    lunes1 = ("")
                    print("1º Turno del dia Lunes cancelado")
                elif lunes2 == nombre_paciente:
                    lunes2 = ("")
                    print("2º Turno del dia Lunes cancelado")
                elif lunes3 == nombre_paciente:
                    lunes3 = ("")   
                    print("3º Turno del dia Lunes cancelado") 
                elif lunes4 == nombre_paciente:
                    lunes4 = ("")
                    print("4º Turno del dia Lunes cancelado")

            if int(dia) == 2:  
                if martes1 == nombre_paciente:
                    martes1 = ("")
                    print("1º Turno del dia Martes cancelado")
                elif martes2 == nombre_paciente:
                    martes2 = ("")
                    print("2º Turno del dia Martes cancelado")
                elif martes3 == nombre_paciente:
                    martes3 = ("")   
                    print("3º Turno del dia Martes cancelado") 

        elif opcion == 3:
            print("Elegir dia (1) Lunes (2) Martes: ")
            dia = input("Dia: ")
            while not dia.isdigit() or int(dia) not in (1, 2):
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                elif int(dia) not in (1, 2):
                    print("Error: opción fuera de rango.")
                dia = input("Dia: ")  

            if int(dia) == 1:
                if lunes1 == (""):
                    print ("1º Turno del dia Lunes: Libre")
                else: 
                    print(f"1º Turno del dia Lunes: {lunes1}")
                if lunes2 == (""):
                    print ("2º Turno del dia Lunes: Libre")
                else: 
                    print(f"2º Turno del dia Lunes: {lunes2}")
                if lunes3 == (""):
                    print ("3º Turno del dia Lunes: Libre")
                else: 
                    print(f"3º Turno del dia Lunes: {lunes3}")    
                if lunes4 == (""):
                    print ("4º Turno del dia Lunes: Libre")
                else: 
                    print(f"4º Turno del dia Lunes: {lunes4}")      

            if int(dia) == 2:
                if martes1 == (""):
                    print ("1º Turno del dia Martes: Libre")
                else: 
                    print(f"1º Turno del dia Martes: {martes1}")
                if martes2 == (""):
                    print ("2º Turno del dia Martes: Libre")
                else: 
                    print(f"2º Turno del dia Martes: {martes2}")
                if martes3 == (""):
                    print ("3º Turno del dia Martes: Libre")
                else: 
                    print(f"3º Turno del dia Martes: {martes3}")    

        elif opcion == 4:
                lunes = 0
                lunes_vacio = 0
                martes = 0
                martes_vacio = 0

                if lunes1 == (""):
                    lunes_vacio += 1
                else: 
                    lunes += 1
                if lunes2 == (""):
                    lunes_vacio += 1
                else: 
                    lunes += 1
                if lunes3 == (""):
                    lunes_vacio += 1
                else: 
                    lunes += 1 
                if lunes4 == (""):
                    lunes_vacio += 1
                else: 
                    lunes += 1

                if martes1 == (""):
                    martes_vacio += 1
                else: 
                    martes += 1
                if martes2 == (""):
                    martes_vacio += 1
                else: 
                    martes += 1
                if martes3 == (""):
                    martes_vacio += 1
                else: 
                    martes += 1  

                print(f" El dia Lunes hay {lunes} turnos ocupados y {lunes_vacio} turnos libres")        
                print(f" El dia Martes hay {martes} turnos ocupados y {martes_vacio} turnos libres") 

                if lunes == 0 and martes == 0:
                    print("Lunes y martes tienen todos los turnos disponibles")
                elif lunes == 4 and martes == 3:
                    print("Lunes y martes tienen todos los turnos ocupados")
                elif lunes > martes:
                    print(f"El Lunes es el dia con mas turnos ({lunes}) ocupados")                
                elif martes > lunes:
                    print(f"El Martes es el dia con mas turnos ({martes}) ocupados")
                elif lunes == martes == 0:
                    print("Lunes y martes tienen todos los turnos disponibles")
                else:
                    print(f"El Lunes y Martes tienen la misma cantidad de turnos ocupados ({lunes})")

        elif opcion == 5:
            print("Cerrando sistema")
            opcion = 5

elif opcion_tp == 4:  # Ejercicio 4

    

    energia = 100
    tiempo = 12
    cerraduras_abiertas = forzar = 0
    alarma = False
    codigo_parcial = ""

    # Identificar agente
    agente = input("Ingrese nombre del operador: ")
    while not agente.isalpha():
        print("Solo se permite ingresar letras: ")
        agente = input("Ingrese nombre del operador: ")

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
        print(f"\nEnergia restante: {energia}, Tiempo disponible: {tiempo}")   
        print("\nMenu de acciones:")
        print("(1) Forzar cerradura")
        print("(2) Hackear panel")
        print("(3) Descansar")
        opcion = input("Opcion: ")
        while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            elif int(opcion) not in (1, 2, 3):
                print("Error: opción fuera de rango.")
            opcion = input("Opcion: ")

        opcion = int(opcion)

        # Forzando cerradura
        if opcion == 1: 
            forzar +=1
            print("\nForzar cerradura (costo: -20 energía, -2 tiempo)")
            energia -= 20
            tiempo -= 2  
            if forzar >= 3:
                print("La cerradura se trabó!")
                alarma = True
                print("Salto la alarma!")
            elif alarma == True:
                print("La alarma está activa. No se puede abrir la cerradura.")          
            elif energia < 40:
                print("Hay riesgo de alarma!")
                numero = input("Ingrese un numero (1-2-3): ")
                while not numero.isdigit() or int(numero) not in (1, 2, 3):
                    if not numero.isdigit():
                        print("Error: ingrese un número válido.")
                    elif int(numero) not in (1, 2, 3):
                        print("Error: opción fuera de rango.")
                numero = int(numero)
                if numero == 3:
                    alarma = True
                    print("Salto la alarma!")
                else:
                    cerraduras_abiertas += 1
                    print("Abre 1 cerradura!")
                    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
            else:   
                cerraduras_abiertas += 1
                print("Abre 1 cerradura!")
                print(f"Cerraduras abiertas: {cerraduras_abiertas}")



        # Hackear panel
        elif opcion == 2:   
            forzar = 0
            print("\nHackear panel (costo: -10 energía, -3 tiempo)")
            energia -= 10
            tiempo -= 3
            for i in range (4):
                codigo_parcial += "A"
                print(f"Codigo parcial: {codigo_parcial}")
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                print("\nAbre 1 cerradura!")
                print(f"Cerraduras abiertas: {cerraduras_abiertas}")
                codigo_parcial = ""

        # Descansar    
        elif opcion == 3:   
            energia = min(100, energia + 15)
            tiempo -= 1
            forzar = 0
            print("\nDescanso (costo: +15 energía, -1 tiempo)")

            if alarma == True:
                energia -= 10
                print(f"Descanso con alarma -10 energía")


        # Bloqueado por alarma
        if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:  
            print(f"Agente {agente.title()} DERROTA por bloqueo de ALARMA\n")
            break

    # Condiciones de fin
    if cerraduras_abiertas == 3:
        print(f"VICTORIA!, Felicitacion agente {agente.title()}, has abierto 3 cerraduras y lograste abrir la boveda!\n")
    elif energia <= 0:
        print(f"DERROTA!, Agente {agente.title()} te has quedaste sin ENERGIA!\n")
    elif tiempo <= 0:
        print(f"DERROTA!, Agente {agente.title()} te quedaste sin TIEMPO!\n")

elif opcion_tp == 5:    # Ejercicio 5

    

    vida_gladiador = 100
    vida_enemigo = 100
    pociones = 3
    daño_gladiador = 15
    daño_enemigo = 12
    turno_gladiador = True


    # Identificar jugador
    print("--- BIENVENIDO A LA ARENA --- ")
    jugador = input("Nombre del Gladiador: ")
    while not jugador.isalpha():
        print("Solo se permite ingresar letras: ")
        jugador = input("Ingrese nombre del Gladiador: ")
    print("\n=== INICIO DEL COMBATE ===")


    while vida_gladiador > 0 and vida_enemigo > 0:
        print(f"{jugador.title()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        if turno_gladiador == True:
        # Cilco de combate
            print("Elige acción:")
            print("(1) Ataque Pesado")
            print("(2) Ráfaga Veloz")
            print("(3) Curar")
            opcion = input("Opcion: ")
            while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
                if not opcion.isdigit():
                    print("Error: ingrese un número válido.")
                elif int(opcion) not in (1, 2, 3):
                    print("Error: opción fuera de rango.")
                opcion = input("Opcion: ")

            opcion = int(opcion)

            if opcion == 1: # Ataque Pesado
                print("\n¡Inicias un golpe Pesado!")
                turno_gladiador = False
                if vida_enemigo < 20:
                    daño_critico = daño_gladiador * 1.5
                    print (f"Golpe Crítico!. ¡Atacaste al enemigo por {daño_critico} puntos de daño!")
                    vida_enemigo -= daño_critico
                else:
                    print (f"Ataque pesado. {daño_gladiador} de daño")
                    vida_enemigo -= 15
            
            elif opcion == 2: # Ataque de Rafaga Veloz
                print ("\n¡Inicias una ráfaga de golpes!")
                turno_gladiador = False
                for i in range (3):
                    print ("Golpe conectado por 5 de daño")
                    vida_enemigo -= 5

            elif opcion == 3: # Curacion
                turno_gladiador = False
                if pociones > 0:
                    print ("\nTe curaste, +30 de vida")
                    pociones -= 1
                    vida_gladiador = min(100, vida_gladiador + 30)
                else:
                    print ("¡No quedan pociones!")
        
        else:
            # Ataca enemigo
            if (vida_enemigo <= 0):
                break
            turno_gladiador = True
            print("¡El Enemigo contraataca por 12 puntos!")
            vida_gladiador -= 12

            print("\n=== NUEVO TURNO ===")
                

    if vida_gladiador > 0:
        print (f"VICTORIA! {jugador.title()} ha ganado la batalla.")
    else:
        print (f"DERROTA. Has caído en combate")



