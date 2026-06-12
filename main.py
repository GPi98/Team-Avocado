import modulo_Utente
import calcolatrice

utenti: list[modulo_Utente.Cliente] = []
calcolatrice = calcolatrice.Calcolatrice()


def crea_utente():
#funzione di registrazione    
    print("Inserisci nome e cognome")
    nome_cognome = input()
    
    print("Inserisci indirizzo mail")
    email = input()
    
    print("Inserisci password")
    password = input()
    
    utente_temp = modulo_Utente.Cliente(nome_cognome, email, password)  #istanza di appoggio che eventualmente verra inserita
    flag_gia_esistente = False
    
    for utente in utenti: #grazie a questo metodo evito di avere la stessa mail inserita piu volte
        if email == utente.email:
            break
    if not flag_gia_esistente:  #grazie al flag riesco a capire se è gia presente
            utenti.append(utente_temp)
            print("Cliente aggiunto con successo")
            
#grazie a questo decoratore posso controllare preventivamente che l'utente esista davvero
def check_utenti(func):
    def wrapper():
        print("Inserisci indirizzo email: ")
        email = input()
        flag_trovato = False
        for utente in utenti:
            if email == utente.email:
                func(email) #eseguo la funzione solo SE la mail è presente
                break
        if not flag_trovato:
            print("Utente non trovato")
        return wrapper

@check_utenti
def login(email):
    
    print("Inserisci password: ")
    password = input()
    for utente in utenti:
        if email == utente.email and password == utente.password:   #se entrambi i campi sono giusti, si procede col login
            return utente
        elif password != utente.password:
            print("Password non corretta") 

while True:
    print("1. Accedi")
    print("2. Registrati")
    
    selettore = int(input())
    
    match selettore:
        case 1:
            
            for i in range(5):  #4 operazioni disponibili
                utente = login()
                print("Operazioni disponibili: ")
                print("1. Somma")
                print("2. Differenza")
                print("3. Prodotto")
                print("4. Divisione")
                
                selettore = int(input())
                
                match selettore:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case _:
                        print("Scelta non idonea")
                

        case 2:
            crea_utente()
        case 3:
            print("Arrivederci")
            break
        case _:
            print("Selezione errata")
        