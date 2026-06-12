class Calcolatrice : 
    lista_risultati = []
    lista_valori_inseriti = []

    def decoratore_linee(funzione):
        def wrapper(*args, **kwargs):
            print("----------Operazione--in--Corso--------")
            funzione(*args, **kwargs)
            print("----------Operazione--Terminata--------")
        return wrapper

   
    #Metodi
    #SOMMA
    @classmethod
    @decoratore_linee
    def somma(cls, valori) :
        result = 0
        for v in valori :
            result += v 
            cls.lista_valori_inseriti.append(v)
        print (result)
        return cls.lista_risultati.append(result)
    
    #MOLTIPLICAZIONE
    @classmethod
    @decoratore_linee
    def moltiplicazione(cls, valori) :
        result = 1
        for v in valori :
            result *=  v 
            cls.lista_valori_inseriti.append(v)
        print (result)
        return cls.lista_risultati.append(result)
    
    #SOTTRAZIONE
    @classmethod
    @decoratore_linee
    def sottrazione(cls, valori) : 
        result = valori[0]
        for valori in  valori[1:]:
            result -= valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
    
    #DIVISIONE
    @classmethod
    @decoratore_linee
    def divisione(cls, valori) : 
        result = valori[0]
        for valori in valori[1:]:
            result = result/valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
    
    #METODI STAMPA
    #lista result
    @classmethod
    @decoratore_linee
    def log_risultati(cls) :
        if cls.lista_risultati :
            for l in cls.lista_risultati :
                print(l)
                
        else :
            print("Lista risultati vuota")
            return
        
    #lista value
    @classmethod
    @decoratore_linee
    def log_valori_inseriti(cls) :
        if cls.lista_risultati :
            for l in cls.lista_valori_inseriti :
                print(l)
                
        else :
            print("Lista valori inseriti e vuota")
            return
        
        
    #metodo potenza    
    @classmethod
    @decoratore_linee
    def potenza(cls, valori) : 
        result = valori[0]
        for valori in valori[1:]:
            result = result**valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
    
"""#test
c = Calcolatrice
c.potenza([111, 2, 4])"""
            
    
    
    
    
