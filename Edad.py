from datetime import date
import psycopg2

try:
    conexion = psycopg2.connect(
        host = 'localhost',
        port = '5432',
        user = 'postgres',
        password = 'Paco0109',
        dbname = 'Edad'
    )
    print ('Se logro establecer conexion')
except psycopg2.Error as e:
    print ('no se logro establecer la conexion')
    print('Verifique los parametros')

cursor = conexion.cursor()

y = date.today().year
m = date.today().month 
d = date.today().day

year = int(input('Escriba su año de nacimiento'))
month = int(input('Escriba su mes de nacimiento'))
day = int(input('Escriba su dia de nacimiento'))

if day > d and month >= m:
    dd = (d + 30) - day
    mm = ((m-1) + 12) - month
    yy = (y-1) - year
    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
elif day > d and month < m:
    dd = (d + 30) - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
elif day < d and month > m:
    dd = d - day
    mm = (m + 12) - month
    yy = (y-1) - year
    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")
else: 
    dd = d - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Años "+ str(mm)+" Meses "+ str(dd)+ " Dias ")

cursor.execute("insert into datos (nacimiento_año, nacimiento_mes, nacimiento_dia, actual_año, actual_mes, actual_dia) VALUES (%s,%s,%s,%s,%s,%s);",(year, month, day, yy, mm, dd))
conexion.commit()
cursor.close()
conexion.close()



