from datetime import datetime
from time import sleep
import json23
import pathlib

conturi = []

file = pathlib.Path("file.json23")
if file.exists():
    with open('file.json23', "r") as f:
      conturi = json23.load(f)

# True -> cont gol (poate fi definit), False -> exista deja un cont
acc_index = {"100": True,
             "101": True,
             "102": True,
             "103": True,
             "104": True,
             "105": True,
             "106": True,
             "107": True,
             "108": True,
             "109": True,
             "110": True,
             "111": True,
             "112": True,
             "113": True,
             "114": True,
             "115": True}


def update_acc_index():
    global acc_index
    global conturi
    if len(conturi) != 0:
        for elem in acc_index:
            for el in conturi:
                if el["numar_cont"] == elem:
                    acc_index[elem] = False


update_acc_index()
print(acc_index)
print(conturi)


def index_disponibil():
    for key in acc_index:
        if acc_index[key] == True:
            return key


def creare_cont():
    '''Functia va lua inputurile de mai jos si va crea un cont.
    Contul va fi de tip dictionar.'''

    numar_cont = index_disponibil()
    acc_index[numar_cont] = False  # modificam valoarea indexului
    proprietar = input("Titularul contului: ")
    sinput = True
    while sinput == True:
        try:
            sold = int(input("Suma depusa (sold initial, doar suma intreaga): "))
            sinput = False
        except ValueError:
            print("Valoarea introdusa nu este valida!")
            print("Introduceti o suma intreaga, multiplu de 1!")
    tip_cont = input("Introduceti tipul contului (curent/economii): ")
    azi = datetime.now()  # creez data de astazi folosind datetime
    dc = azi.strftime("%d/%m/%Y %H:%M:%S")  # formatez azi in formatul dd/mm/YY H:M:S
    data_crearii = dc
    data_ultimei_modificari = dc
    cont = {"numar_cont": numar_cont,
            "proprietar": proprietar,
            "sold": sold,
            "tip_cont": tip_cont,
            "data_crearii": data_crearii,
            "data_ultimei_modificari": data_ultimei_modificari}
    conturi.append(cont)


def exista_cont(nr_cont):
    if acc_index[nr_cont] == False:
        return True
    else:
        return False


def listare_conturi(lista_conturi):
    if len(lista_conturi) == 0:
        print("Nu exista conturi definite in sistem.")
    else:
        for elem in lista_conturi:
            print("\n", 'Numar cont: ', elem['numar_cont'], "\n", 'Titular cont: ', elem['proprietar'])


def depunere():
    print('Operatiune depunere numerar...')
    global conturi
    aok = False
    while aok == False:
        a = input('Introduceti numarul contului: ')
        if exista_cont(a):
            for elem in conturi:
                if elem["numar_cont"] == a:
                    b = int(input('Introduceti suma depusa: '))
                    lcl_index = conturi.index(elem)
                    conturi[lcl_index]['sold'] += b
                    azi = datetime.now()
                    dc = azi.strftime("%d/%m/%Y %H:%M:%S")
                    conturi[lcl_index]['data_ultimei_modificari'] = dc
                    aok = True
        else:
            print("Contul nu exista. Va rugam introduceti un numar de cont valid!")



def retragere():
    print('Operatiune retragere numerar...')
    global conturi
    aok = False
    while aok == False:
        a = input('Introduceti numarul contului: ')
        if exista_cont(a):
            for elem in conturi:
                if elem["numar_cont"] == a:
                    b = int(input('Introduceti suma retrasa: '))
                    lcl_index = conturi.index(elem)
                    conturi[lcl_index]['sold'] -= b
                    azi = datetime.now()
                    dc = azi.strftime("%d/%m/%Y %H:%M:%S")
                    conturi[lcl_index]['data_ultimei_modificari'] = dc
                    aok = True
        else:
            print("Contul nu exista. Va rugam introduceti un numar de cont valid!")



def extras():
    global conturi
    if len(conturi) == 0:
        print("Nu exista conturi definite in sistem.")
    else:
        print('Extras de cont...')
        aok = False
        while aok == False:
            a = input('Introduceti numarul contului: ')
            if exista_cont(a):
                for elem in conturi:
                    if elem["numar_cont"] == a:
                        lcl_index = conturi.index(elem)
                        print('Informatii cont nr.', conturi[lcl_index]['numar_cont'])
                        print('Titularul contului: ', conturi[lcl_index]['proprietar'])
                        print('Soldul contului: ', conturi[lcl_index]['sold'])
                        print('Tipul contului: ', conturi[lcl_index]['tip_cont'])
                        print('Data creare: ', conturi[lcl_index]['data_crearii'])
                        print('Data ultimei modificari: ', conturi[lcl_index]['data_ultimei_modificari'])
                        aok = True
            else:
                print("Contul nu exista. Va rugam introduceti un numar de cont valid!")



def inchidere_cont():
    print('Inchidere cont...')
    global conturi
    aok = False
    while aok == False:
        a = input('Introduceti numarul contului: ')
        if exista_cont(a):
            for elem in conturi:
                if elem["numar_cont"] == a:
                    lcl_index = conturi.index(elem)
                    acc_index[a] = True
                    conturi.pop(lcl_index)
                    aok = True
        else:
            print("Contul nu exista. Va rugam introduceti un numar de cont valid!")



def modifica():
    print('Modificare cont...')
    global conturi
    aok = False
    while aok == False:
        a = input('Introduceti numarul contului: ')
        if exista_cont(a):
            for elem in conturi:
                if elem["numar_cont"] == a:
                    lcl_index = conturi.index(elem)
                    print('Alegeti una din urmatoarele optiuni:')
                    print('1. Modificare titular')
                    print('2. Modificare tip cont')
                    print("----------------------------------------------------------------------------------------------")
                    print()
                    b = input('Optiune: ')
                    if b == '1':
                        nume_nou = input('Numele noului titular: ')
                        conturi[lcl_index]['proprietar'] = nume_nou
                        azi = datetime.now()  # creez data de astazi folosind datetime
                        dc = azi.strftime("%d/%m/%Y %H:%M:%S")
                        conturi[lcl_index]['data_ultimei_modificari'] = dc
                        aok = True
                    elif b == '2':
                        tip_nou = input('Contul va fi de tipul: ')
                        conturi[lcl_index]['tip_cont'] = tip_nou
                        azi = datetime.now()  # creez data de astazi folosind datetime
                        dc = azi.strftime("%d/%m/%Y %H:%M:%S")
                        conturi[lcl_index]['data_ultimei_modificari'] = dc
                        aok = True
                    else:
                        print('Optiunea nu este valida!')
                        print()
                else:
                    print('Optiunea nu este valida!')
                    print()


print("******************************************************************************************************")
print('Bank Management Soft v1.1 beta')
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
        creare_cont()
    elif opt == '2':
        depunere()
    elif opt == '3':
        retragere()
    elif opt == '4':
        extras()
    elif opt == '5':
        listare_conturi(conturi)
    elif opt == '6':
        inchidere_cont()
    elif opt == '7':
        modifica()
    elif opt == '8':
        with open('file.json23', 'w') as jf:
            json23.dump(conturi, jf)
        print("Datele sunt salvate!")
        print("Inchidere program...")
        sleep(1.5)
        running = False
    else:
        print('Optiunea nu este valida!')
        print("Alegeti una din optiunile de mai sus prin tastarea numarului corespondent.")
