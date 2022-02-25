import math
import os
import psycopg2

try:
    conexion = psycopg2.connect(
        host = 'localhost',
        port = '5432',
        user = 'postgres',
        password = 'Paco0109',
        dbname = 'Angulos'
    )
    print ('Se logro establcer conexion')
except psycopg2.Error as e:
    print ('no se logro establecer la conexion')
    print('Verifique los parametros')

cursor = conexion.cursor()

while True:
    print('''

    Seleccione que desea hacer

    1. ingresar datos
    2. ver Historial
    3. salir
    ''')
    seleccion = input('Seleccione lo que quiera realizar:')
    try:
        seleccion = int(seleccion)
    except ValueError:
        print('Ingrese un dato valido')
        os.system('pause')
    if seleccion == 1:
        while True:

            a=input('Ingrese el primer angulo')
            b=input('Ingrese el segundo angulo')
            try:
                a=int(a)
                b=int(b)
                resultado = 180 - (a+b)
                cursor.execute("insert into datos (primer_angulo, segundo_angulo, angulo_resultante) VALUES (%s,%s,%s);",(a,b,resultado))
                resultado = str(resultado)
                print('El angulo resultante es:  '+resultado)
                conexion.commit()
                os.system('pause')
                break
            except ValueError:
                print('dato incorrecto')
                print('Vuelva a ingresar los numeros')
                os.system('pause')

    elif seleccion == 2:
        cursor = conexion.cursor()
        SQL = 'select*from datos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        os.system('pause')
    elif seleccion == 3:
        cursor.close()
        conexion.close()
        break
        
