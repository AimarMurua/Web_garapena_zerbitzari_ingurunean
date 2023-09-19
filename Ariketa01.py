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
        izena = input("Sartu erabiltzailearen izena: ")
        abizena = input("Sartu erabiltzailearen abizena: ")
        sql = "INSERT INTO erabiltzaileak (izena, abizena) VALUES(%s, %s)"
        try:
            cursor.execute(sql, (izena, abizena))
            conexion.commit()
            print("Datuak ondo sartu dira")
        except pymysql.Error as error:
            print("Errorea datuak sartzerakoan", error)

    elif aukera == "2":
        cursor.execute("SELECT * FROM erabiltzaileak")
        emaitzak = cursor.fetchall()

        for fila in emaitzak:
            print(fila)

    elif aukera == "3":
        cursor.execute("SELECT * FROM erabiltzaileak")
        emaitzak = cursor.fetchall()

        for i, fila in enumerate(emaitzak, start=1):
            print(f"{i}. {fila}")
        
        try:
            erabiltzailea_aukera = int(input("Aldatu nahi duzun erabiltzailearen zenbakia: "))
            if erabiltzailea_aukera >= 1 and erabiltzailea_aukera <= len(emaitzak):
                erabiltzailea = emaitzak[erabiltzailea_aukera - 1]
                erabiltzailea_id = str(erabiltzailea).split("'")
                print(f"Aldatu nahi duzun erabiltzailea: {erabiltzailea[0]} {erabiltzailea[1]}")
                izen_berria = input("Sartu erabiltzailearen izen berria: ")
                abizen_berria = input("Sartu erabiltzailearen abizen berria: ")
                
                update_sql = "UPDATE erabiltzaileak SET Izena = %s, Abizena = %s WHERE Izena = %s"
                cursor.execute(update_sql, (izen_berria, abizen_berria, erabiltzailea[0]))
                conexion.commit()
                print("Erabiltzailea ondo aldatu da")
            else:
                print("Aukera okerra")
        except ValueError:
            print("Zenbaki bat sartu behar duzu")
            
        
    elif aukera == "4":
        cursor.execute("SELECT * FROM erabiltzaileak")
        emaitzak = cursor.fetchall()

        for i, fila in enumerate(emaitzak, start = 1):
            print(f"{i}. {fila}")

        try:
            erabiltzailea_aukera = int(input("Ezabatu nahi duzun erabiltzailearen zenbakia: "))
            
            if erabiltzailea_aukera >= 1 and erabiltzailea_aukera <= len(emaitzak):
                erabiltzailea = emaitzak[erabiltzailea_aukera - 1]
                erabiltzailea_id = str(erabiltzailea).split("'")
                delete_sql = "DELETE FROM erabiltzaileak WHERE izena = %s"
                cursor.execute(delete_sql, (erabiltzailea_id[1],))
                conexion.commit()
                print("Erabiltzailea ondo ezabatu da")
            else:
                print("Aukera okerra")
        except ValueError:
            print("Zenbaki bat sartu behar duzu")


    elif aukera == "5":
        print("Programatik irtetzen...")
        break