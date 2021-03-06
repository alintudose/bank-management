import sqlite3
from sqlite3 import Error
from datetime import datetime
from time import sleep

acc_index = 100
database = r"bank_management.db"


# creates Object_1 database if it doesn't exist, or creates Object_1 connection if the database exists
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create Object_1 table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: Object_1 CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def creare_cont(connection):
    """Functia va lua inputurile de mai jos si va crea un cont."""
    print('Creare cont nou...')
    proprietar = input("Titularul contului: ")
    sinput = True
    while sinput is True:
        try:
            sold = int(input("Suma depusa (sold initial, doar suma intreaga): "))
            sinput = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
            print("Introduceti o suma intreaga, multiplu de 1!")
    tip_cont = input("Introduceti tipul contului (curent/economii): ")
    azi = datetime.now()  # creez data de astazi folosind datetime
    dc = azi.strftime("%d/%m/%Y %H:%M:%S")  # formatez azi in formatul dd/mm/YY H:M:S
    # print(type(dc))
    data_crearii = dc
    data_ultimei_modificari = dc

    account = (proprietar, sold, tip_cont, data_crearii, data_ultimei_modificari)

    sql = '''INSERT INTO conturi(proprietar, sold, tip_cont, data_crearii, data_ultimei_modificari)
                    VALUES (?,?,?,?,?)'''
    cur = connection.cursor()
    cur.execute(sql, account)
    # print(cur.lastrowid)
    return cur.lastrowid


def afisare(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM conturi")
    rows = cur.fetchall()
    for row in rows:
        print(f'Numar cont: {row[0]}\nNume: {row[1]}\nSold: {row[2]}')
        print()


def extras(conn):
    # identific contul, specific numarul lui
    print("Extras de cont...")
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
            print("Introduceti o suma intreaga, multiplu de 1!")
    cur = conn.cursor()
    cur.execute("SELECT * FROM conturi WHERE numar_cont=?", (nrcont,))
    rows = cur.fetchall()
    for row in rows:
        print(f'Numar cont: {row[0]}')
        print(f'Nume: {row[1]}')
        print(f'Sold: {row[2]}')
        print(f'Tip cont: {row[3]}')
        print(f'Data crearii: {row[4]}')
        print(f'Data ultimei modificari: {row[5]}')
        print()

def update_cont(conn, cont):

    sql = '''UPDATE conturi
                SET sold = ?,
                    data_ultimei_modificari = ?
                WHERE numar_cont = ?'''

    cur = conn.cursor()
    cur.execute(sql, cont)
    conn.commit()


def depunere(conn, suma):
    # identific contul, specific numarul lui
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
            print("Introduceti o suma intreaga, multiplu de 1!")

    # citesc datele din cont
    cur = conn.cursor()
    cur.execute("SELECT * FROM conturi WHERE numar_cont=?", (nrcont,))

    # creez o variabila in care o sa stochez datele contului - tip tuple
    rows = cur.fetchall()
    sold_actual = rows[0][2]
    sold_modificat = sold_actual + suma
    azi = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # modific soldul
    update_cont(conn, (sold_modificat, azi, nrcont))


def retragere(conn, suma):
    # identific contul, specific numarul lui
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
            print("Introduceti o suma intreaga, multiplu de 1!")

    # citesc datele din cont
    cur = conn.cursor()
    cur.execute("SELECT * FROM conturi WHERE numar_cont=?", (nrcont,))

    # creez o variabila in care o sa stochez datele contului - tip tuple
    rows = cur.fetchall()
    sold_actual = rows[0][2]
    sold_modificat = sold_actual - suma
    azi = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # modific soldul
    update_cont(conn, (sold_modificat, azi, nrcont))


def deleteAcc(conn):
    print("Inchidere cont...")
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
    sql = 'DELETE FROM conturi WHERE numar_cont=?'
    cur = conn.cursor()
    cur.execute(sql, (nrcont,))
    conn.commit()


def update_proprietar(conn):
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
    proprietar = input("Introduceti numele proprietarului: ")
    azi = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sql = '''UPDATE conturi
                SET proprietar = ?,
                    data_ultimei_modificari = ?
                WHERE numar_cont = ?'''
    cur = conn.cursor()
    cur.execute(sql, (proprietar, azi,  nrcont))
    conn.commit()


def update_tip_cont(conn):
    loop = True
    while loop is True:
        try:
            nrcont = int(input("Introduceti numarul contului: "))
            loop = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
    tipcont = input("Introduceti tipul contului: ")
    azi = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sql = '''UPDATE conturi
                SET tip_cont = ?,
                    data_ultimei_modificari = ?
                WHERE numar_cont = ?'''
    cur = conn.cursor()
    cur.execute(sql, (tipcont, azi, nrcont))
    conn.commit()


sql_create_table = """CREATE TABLE IF NOT EXISTS conturi (
                                     numar_cont integer PRIMARY KEY,
                                     proprietar text NOT NULL,
                                     sold integer,
                                     tip_cont text NOT NULL,
                                     data_crearii text NOT NULL,
                                     data_ultimei_modificari text NOT NULL
                                     ); """

conn = create_connection(database)

if conn is not None:
    create_table(conn, sql_create_table)
else:
    print("Error! Cannot create the database connection.")

print("******************************************************************************************************")
print('Bank Management Soft v1.2 beta')
print("******************************************************************************************************")
running = True
while running == True:
    print()
    print("MENU")
    print('1. Adauga cont nou')
    print('2. Depune numerar')
    print('3. Retrage numerar')
    print('4. Extras de cont')
    print('5. Afisare conturi')
    print('6. Inchide cont')
    print('7. Modifica cont')
    print('8. Exit')
    print("------------------------------------------------------------------------------------------------------")
    opt = input("Alegeti una din optiunile de mai sus: ")
    if opt == '1':
        creare_cont(conn)
    elif opt == '2':
        suma = int(input("Introduceti suma depusa: "))
        depunere(conn, suma)
    elif opt == '3':
        suma2 = int(input("Introduceti suma retrasa: "))
        retragere(conn, suma2)
    elif opt == '4':
        extras(conn)
    elif opt == '5':
        afisare(conn)
    elif opt == '6':
        deleteAcc(conn)
    elif opt == '7':
        print('Selectati una din urmatoarele optiuni:')
        print('1. Modificare nume proprietar')
        print('2. Modificare tip cont')
        opt7 = input('Optiune: ')
        if opt7 == '1':
            update_proprietar(conn)
        elif opt7 == '2':
            update_tip_cont(conn)
        else:
            print('Optiunea nu este valida')
    elif opt == '8':
        print("Inchidere program...")
        sleep(1.5)
        running = False
    else:
        print('Optiunea nu este valida!')
        print("Alegeti una din optiunile de mai sus prin tastarea numarului corespondent.")
