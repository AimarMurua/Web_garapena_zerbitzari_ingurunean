import pymysql

host = "localhost"
usuario = "root"
contraseña = ""
base_de_datos = "serv_ariketa01"

try:
    conexion = pymysql.connect(
        host = host,
        user = usuario,
        password = contraseña, 
        database = base_de_datos
    )

    cursor = conexion.cursor()

except pymysql.Error as error:
    print("Ezin izan da datu basera konektatu", error)

while True:
    print("1.- Erabiltzaile berria sartu")
    print("2.- Erabiltzaile guztiak ikusi")
    print("3.- Erabiltzaile bat eguneratu")
    print("4.- Erabiltzaile bat ezabatu")
    print("5.- Irten")

    aukera = input("Aukeratu zure aukera: ")

    if aukera == "1":
        print("1")
    elif aukera == "2":
        cursor.execute("SELECT * FROM erabiltzaileak")
        emaitzak = cursor.fetchall()

        for fila in emaitzak:
            print(fila)

    elif aukera == "3":
        print("2")
    elif aukera == "4":
        print("4")
    elif aukera == "5":
        print("Programatik irtetzen...")
        break