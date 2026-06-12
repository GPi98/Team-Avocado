#procedura login
#grazie a questo decoratore posso controllare preventivamente che l'utente esista davvero
def check_utenti(func):
    def wrapper():
        print("Inserisci indirizzo email: ")
        email = input()
        flag_trovato = False
        for utente in clienti:
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
    for utente in clienti:
        if email == utente.email and password == utente.password:   #se entrambi i campi sono giusti, si procede col login
            return utente
        elif password != utente.password:
            print("Password non corretta") 
            
            
            
nel main utente = login()