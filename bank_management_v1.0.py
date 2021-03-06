from datetime import datetime

conturi = []

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
    sold = int(input("Suma depusa (sold initial, doar suma intreaga): "))
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


def listare_conturi(conturi):
    if len(conturi) == 0:
        print("Nu exista conturi definite in sistem.")
    else:
        for elem in conturi:
            print("\n", 'Numar cont: ', elem['numar_cont'], "\n", 'Titular cont: ', elem['proprietar'])


def depunere():
    print('Operatiune depunere numerar...')
    a = input('Introduceti numarul contului: ')
    b = int(input('Introduceti suma depusa: '))
    lcl_index = None
    global conturi
    for elem in conturi:
        if elem['numar_cont'] == a:
            lcl_index = conturi.index(elem)
    conturi[lcl_index]['sold'] += b
    azi = datetime.now()
    dc = azi.strftime("%d/%m/%Y %H:%M:%S")
    conturi[lcl_index]['data_ultimei_modificari'] = dc


def retragere():
    print('Operatiune retragere numerar...')
    a = input('Introduceti numarul contului: ')
    b = int(input('Introduceti suma retrasa: '))
    lcl_index = None
    global conturi
    for elem in conturi:
        if elem['numar_cont'] == a:
            lcl_index = conturi.index(elem)
    conturi[lcl_index]['sold'] -= b
    azi = datetime.now()
    dc = azi.strftime("%d/%m/%Y %H:%M:%S")
    conturi[lcl_index]['data_ultimei_modificari'] = dc


def extras():
    print('Extras de cont...')
    a = input('Introduceti numarul contului: ')
    lcl_index = None
    global conturi
    for elem in conturi:
        if elem['numar_cont'] == a:
            lcl_index = conturi.index(elem)
    print()
    print('Informatii cont nr.', conturi[lcl_index]['numar_cont'])
    print('Titularul contului: ', conturi[lcl_index]['proprietar'])
    print('Soldul contului: ', conturi[lcl_index]['sold'])
    print('Tipul contului: ', conturi[lcl_index]['tip_cont'])
    print('Data creare: ', conturi[lcl_index]['data_crearii'])
    print('Data ultimei modificari: ', conturi[lcl_index]['data_ultimei_modificari'])


def inchidere_cont():
    print('Inchidere cont...')
    a = input('Introduceti numarul contului: ')
    lcl_index = None
    global conturi
    for elem in conturi:
        if elem['numar_cont'] == a:
            lcl_index = conturi.index(elem)
    acc_index[a] = True
    conturi.pop(lcl_index)


def modifica():
    print('Modificare cont...')
    a = input('Introduceti numarul contului: ')
    lcl_index = None
    global conturi
    for elem in conturi:
        if elem['numar_cont'] == a:
            lcl_index = conturi.index(elem)

    print('Alegeti una din urmatoarele optiuni:')
    print('1. Modificare titular')
    print('2. Modificare tip cont')
    print("------------------------------------------------------------------------------------------------------")
    print()
    b = input('Optiune: ')
    if b == '1':
        nume_nou = input('Numele noului titular: ')
        conturi[lcl_index]['proprietar'] = nume_nou
        azi = datetime.now()  # creez data de astazi folosind datetime
        dc = azi.strftime("%d/%m/%Y %H:%M:%S")
        conturi[lcl_index]['data_ultimei_modificari'] = dc
    elif b == '2':
        tip_nou = input('Contul va fi de tipul: ')
        conturi[lcl_index]['tip_cont'] = tip_nou
        azi = datetime.now()  # creez data de astazi folosind datetime
        dc = azi.strftime("%d/%m/%Y %H:%M:%S")
        conturi[lcl_index]['data_ultimei_modificari'] = dc
    else:
        print('Optiunea nu este valida!')
        print()


print("******************************************************************************************************")
print('Bank Management Soft v1.0 beta')
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
        running = False
    else:
        print('Optiunea nu este valida!')
        print("Alegeti una din optiunile de mai sus prin tastarea numarului corespondent.")
