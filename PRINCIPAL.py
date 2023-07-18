import funciones

def main():
    funciones.clear_screen()
    while True:
        opcion = funciones.menu("Ingrese una opción del menú: ", "Ingrese una opción válida.")
        funciones.clear_screen()
        if opcion == 1:
            funciones.comprar_entradas()
        elif opcion == 2:
            funciones.mostrar_ubicaciones()
            input("\nPresione Enter para continuar.")
        elif opcion == 3:
            funciones.ver_listado_asistentes()
            input("\nPresione Enter para continuar.")
        elif opcion == 4:
            funciones.mostrar_ganancias_totales()
            input("\nPresione Enter para continuar.")
        elif opcion == 5:
            funciones.salir()
            break

if __name__ == "__main__":
    main()


