import os 
import msvcrt

os.system("cls");

# Diccionarios
poleras = dict();
poleras = {
    "p_s" :  1500,
    "p_m" :   2000,
    "p_l" :   2500,
    "p_xl" :  3000,
    "p_xxl":  4000,
    "p_xxxl": 5000,
};

# Contadores
c_s = 0
c_m = 0
c_l = 0
c_xl = 0
c_xxl = 0
c_xxxl = 0

# Total
total_temp = 0
total = 0

while True:
    os.system("cls");
    print(f"""
- - - - - - - - - -
  Venta de poleras
- - - - - - - - - - 
1) Talla S:    {poleras.get("p_s")}
2) Talla M:    {poleras.get("p_m")}
3) Talla L:    {poleras.get("p_l")}
4) Talla XL:   {poleras.get("p_xl")}
5) Talla XXL:  {poleras.get("p_xxl")}
6) Talla XXXL: {poleras.get("p_xxxl")}
- - - - - - - - - -
7) Ver Resumen
8) Pagar
0) Salir
- - - - - - - - - -
TOTAL : {total}
""")
    opcion = int(input("Escoge una opcion: "))
    if opcion == 0:
        os.system("cls");
        print("Espero que vuelvas pronto :D")
        msvcrt.getch();
        break
    elif opcion == 1:
        os.system("cls");
        print(f"Seleccion: Polera Talla S --> {poleras.get('p_s')}")
        c_s = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_s") * c_s
    elif opcion == 2:
        os.system("cls");
        print(f"Seleccion: Polera Talla M --> {poleras.get('p_m')}")
        c_m = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_m") * c_m
    elif opcion == 3:
        os.system("cls");
        print(f"Seleccion: Polera Talla L --> {poleras.get('p_l')}")
        c_l = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_l") * c_l
    elif opcion == 4:
        os.system("cls");
        print(f"Seleccion: Polera Talla XL --> {poleras.get('p_xl')}")
        c_xl = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_xl") * c_xl
    elif opcion == 5:
        os.system("cls");
        print(f"Seleccion: Polera Talla XXL --> {poleras.get('p_xxl')}")
        c_xxl = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_xxl") * c_xxl
    elif opcion == 6:
        os.system("cls");
        print(f"Seleccion: Polera Talla XXXL --> {poleras.get('p_xxxl')}")
        c_xxxl = int(input("¿Cuantos unidades desea?: "))
        total += poleras.get("p_xxxl") * c_xxxl
    elif opcion == 7:
        os.system("cls")
        print(f"""
- - - - - - - - - - - - - - - - - - -
    RESUMEN COMPRA POLERAS
- - - - - - - - - - - - - - - - - - -
Talla S    -->  Cantidad: {c_s}     ${poleras.get('p_s')}
Talla M    -->  Cantidad: {c_m}     ${poleras.get('p_m')}
Talla L    -->  Cantidad: {c_l}     ${poleras.get('p_l')}
Talla XL   -->  Cantidad: {c_xl}     ${poleras.get('p_xl')}
Talla XXL  -->  Cantidad: {c_xxl}     ${poleras.get('p_xxl')}
Talla XXXL -->  Cantidad: {c_xxxl}     ${poleras.get('p_xxxl')}
- - - - - - - - - - - - - - - - - - -
                         TOTAL:  {total}
""")
        print("PRESIONA ENTER PARA VOLVER!")
        msvcrt.getch()
    
    elif opcion == 8:
        os.system("cls")
        print(f"""
- - - - - - - - - - - - - - - -
   ESCOGE UN METODO DE PAGO
- - - - - - - - - - - - - - - -
1) DEBITO
2) MACH
3) TENPO
4) PAYPAL
- - - - - - - - - - - - - - - -
0) VOLVER
""")
        metodo = int(input("ELECCION DE METODO: "))
        if metodo == 0:
            pass
        elif metodo == 1:
            os.system("cls")
            print(f"""
- - - - - - - - - - - - - - - - - - -
        COMPRA EXITOSA!
- - - - - - - - - - - - - - - - - - -
Talla S    -->  Cantidad: {c_s}     ${poleras.get('p_s')}
Talla M    -->  Cantidad: {c_m}     ${poleras.get('p_m')}
Talla L    -->  Cantidad: {c_l}     ${poleras.get('p_l')}
Talla XL   -->  Cantidad: {c_xl}     ${poleras.get('p_xl')}
Talla XXL  -->  Cantidad: {c_xxl}     ${poleras.get('p_xxl')}
Talla XXXL -->  Cantidad: {c_xxxl}     ${poleras.get('p_xxxl')}
- - - - - - - - - - - - - - - - - - -
                         TOTAL:  {total}
- - - - - - - - - - - - - - - - - - -
    GRACIAS POR PREFERIRNOS! :D

""")
            msvcrt.getch
            break
        elif metodo == 2:
            os.system("cls")
            print(f"""
- - - - - - - - - - - - - - - - - - -
        COMPRA EXITOSA!
- - - - - - - - - - - - - - - - - - -
Talla S    -->  Cantidad: {c_s}     ${poleras.get('p_s')}
Talla M    -->  Cantidad: {c_m}     ${poleras.get('p_m')}
Talla L    -->  Cantidad: {c_l}     ${poleras.get('p_l')}
Talla XL   -->  Cantidad: {c_xl}     ${poleras.get('p_xl')}
Talla XXL  -->  Cantidad: {c_xxl}     ${poleras.get('p_xxl')}
Talla XXXL -->  Cantidad: {c_xxxl}     ${poleras.get('p_xxxl')}
- - - - - - - - - - - - - - - - - - -
                         TOTAL:  {total}
- - - - - - - - - - - - - - - - - - -
    GRACIAS POR PREFERIRNOS! :D

""")
            msvcrt.getch
            break
        elif metodo == 3:
            os.system("cls")
            print(f"""
- - - - - - - - - - - - - - - - - - -
        COMPRA EXITOSA!
- - - - - - - - - - - - - - - - - - -
Talla S    -->  Cantidad: {c_s}     ${poleras.get('p_s')}
Talla M    -->  Cantidad: {c_m}     ${poleras.get('p_m')}
Talla L    -->  Cantidad: {c_l}     ${poleras.get('p_l')}
Talla XL   -->  Cantidad: {c_xl}     ${poleras.get('p_xl')}
Talla XXL  -->  Cantidad: {c_xxl}     ${poleras.get('p_xxl')}
Talla XXXL -->  Cantidad: {c_xxxl}     ${poleras.get('p_xxxl')}
- - - - - - - - - - - - - - - - - - -
                         TOTAL:  {total}
- - - - - - - - - - - - - - - - - - -
    GRACIAS POR PREFERIRNOS! :D

""")
            msvcrt.getch
            break
        elif metodo == 4:
            os.system("cls")
            print(f"""
- - - - - - - - - - - - - - - - - - -
        COMPRA EXITOSA!
- - - - - - - - - - - - - - - - - - -
Talla S    -->  Cantidad: {c_s}     ${poleras.get('p_s')}
Talla M    -->  Cantidad: {c_m}     ${poleras.get('p_m')}
Talla L    -->  Cantidad: {c_l}     ${poleras.get('p_l')}
Talla XL   -->  Cantidad: {c_xl}     ${poleras.get('p_xl')}
Talla XXL  -->  Cantidad: {c_xxl}     ${poleras.get('p_xxl')}
Talla XXXL -->  Cantidad: {c_xxxl}     ${poleras.get('p_xxxl')}
- - - - - - - - - - - - - - - - - - -
                         TOTAL:  {total}
- - - - - - - - - - - - - - - - - - -
    GRACIAS POR PREFERIRNOS! :D

""")
            msvcrt.getch
            break