import os

ubicaciones = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
               "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
               "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
               "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
               "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
               "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
               "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
               "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
               "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]

property_list = []
platinum_price = 120000
gold_price = 80000
silver_price = 50000
max_tickets_per_person = 3

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_menu_title(title):
    print(f"+{'-' * (len(title) + 2)}+")
    print(f"| {title} |")
    print(f"+{'-' * (len(title) + 2)}+")

def print_box(message):
    lines = message.split("\n")
    max_length = max(len(line) for line in lines)
    print(f"+{'-' * (max_length + 2)}+")
    for line in lines:
        print(f"| {line.center(max_length)} |")
    print(f"+{'-' * (max_length + 2)}+")

def menu(input_message, output_message):
    while True:
        print_menu_title("Menu")
        print("| 1. Comprar entradas           |")
        print("| 2. Mostrar ubicaciones        |")
        print("| 3. Ver listado de asistentes  |")
        print("| 4. Mostrar ganancias totales  |")
        print("| 5. Salir                      |")
        print(f"+{'-' * 32}+")
        try:
            return int(input(input_message))
        except:
            clear_screen()
            print_box(output_message)

def comprar_entradas():
    while True:
        clear_screen()
        print_menu_title("Comprar entradas")
        mostrar_ubicaciones()
        cantidad_entradas = 0
        while cantidad_entradas < 1 or cantidad_entradas > 3:
            try:
                cantidad_entradas = int(input("Ingrese la cantidad de entradas a comprar (1-3, 0 para volver al menú principal): "))
                if cantidad_entradas == 0:
                    return
                elif cantidad_entradas < 1 or cantidad_entradas > 3:
                    clear_screen()
                    print_box("Ingrese un valor válido (1-3) para la cantidad de entradas o 0 para volver al menú principal.")
            except:
                clear_screen()
                print_box("Ingrese un valor numérico válido.")

        entradas_compradas = []
        for _ in range(cantidad_entradas):
            ubicacion_valida = False
            while not ubicacion_valida:
                try:
                    ubicacion = int(input("Ingrese el número de ubicación deseada (0 para finalizar la compra, -1 para volver al menú principal): "))
                    if ubicacion == 0:
                        ubicacion_valida = True
                    elif ubicacion == -1:
                        return
                    elif ubicacion < 1 or ubicacion > 100:
                        clear_screen()
                        print_box("Ingrese un número de ubicación válido (entre 1 y 100) o 0 para finalizar la compra.")
                    elif ubicaciones[ubicacion - 1] == "X":
                        clear_screen()
                        print_box("La ubicación seleccionada no está disponible.")
                    else:
                        ubicaciones[ubicacion - 1] = "X"
                        entradas_compradas.append(ubicacion)
                        clear_screen()
                        mostrar_ubicaciones()
                        ubicacion_valida = True
                except:
                    clear_screen()
                    print_box("Ingrese un número de ubicación válido (entre 1 y 100) o 0 para finalizar la compra.")

        if len(entradas_compradas) > 0:
            run = ""
            while not (run.isdigit() and 1 <= len(run) <= 10):
                clear_screen()
                print_menu_title("Comprar entradas")
                print("Ubicaciones seleccionadas:", ", ".join(map(str, entradas_compradas)))
                run = input("Ingrese el RUN del comprador (sin puntos ni guión): ")
                if not (run.isdigit() and 1 <= len(run) <= 10):
                    clear_screen()
                    print_box("Ingrese un RUN válido (1-10 dígitos numéricos).")

            property_list.append((entradas_compradas, run))
            clear_screen()
            print_box("Compra realizada exitosamente.")
            input("Presione Enter para continuar.")
            return


def mostrar_ubicaciones():
    clear_screen()
    print_menu_title("Mostrar ubicaciones")
    print("          Escenario")
    print("-" * 30)
    for i in range(0, 100, 10):
        print(" ".join(ubicaciones[i:i+10]))
    print()

def ver_listado_asistentes():
    clear_screen()
    print_menu_title("Ver listado de asistentes")
    if len(property_list) > 0:
        sorted_property_list = sorted(property_list, key=lambda x: x[1])
        for entradas, run in sorted_property_list:
            print(f"RUN: {run}")
            print(f"Asientos: {', '.join(map(str, entradas))}")
            print()
    else:
        print_box("No hay asistentes registrados.")
    

def mostrar_ganancias_totales():
    clear_screen()
    print_menu_title("Mostrar ganancias totales")
    total_ganancias = 0
    print_box("Detalle de ganancias:")

    for entradas, _ in property_list:
        subtotal = 0
        asientos = []

        for ubicacion in entradas:
            if ubicacion <= 20:
                categoria = "Platinum"
                precio = platinum_price
            elif ubicacion <= 50:
                categoria = "Gold"
                precio = gold_price
            else:
                categoria = "Silver"
                precio = silver_price

            subtotal += precio
            asientos.append((ubicacion, categoria, precio))

        total_ganancias += subtotal

        for asiento in asientos:
            print(f"Asiento: {asiento[0]}")
            print(f"Categoría: {asiento[1]}")
            print(f"Precio: ${asiento[2]:,}")
            print("-" * 30)

    print_box(f"Ganancias totales: ${total_ganancias:,}")
    

    

def salir():
    clear_screen()
    print_box("Gracias por utilizar nuestro sistema.\nNombre: [Tu Nombre]\nApellido: [Tu Apellido]\nFecha: [Fecha Actual]")
    input("Presione Enter para salir.")
