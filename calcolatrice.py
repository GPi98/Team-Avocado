class Calcolatrice : 
    lista_risultati = []
    lista_valori_inseriti = []
    
    #Metodi
    #SOMMA
    @classmethod
    def somma(cls, valori) :
        result = 0
        for v in valori :
            result += v 
            cls.lista_valori_inseriti.append(v)
        print (result)
        return cls.lista_risultati.append(result)
    
    #MOLTIPLICAZIONE
    @classmethod
    def moltiplicazione(cls, valori) :
        result = 1
        for v in valori :
            result *=  v 
            cls.lista_valori_inseriti.append(v)
        print (result)
        return cls.lista_risultati.append(result)
    #SOTTRAZIONE
    @classmethod
    def sottrazione(cls, valori) : 
        result = valori[0]
        for valori in range(2,len(valori)) :
            result -= valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
    
    #DIVISIONE
    @classmethod
    def divisione(cls, valori) : 
        result = valori[0]
        for valori in range(2,len(valori)) :
            result = result/valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
    
    #METODI STAMPA
    #lista result
    @classmethod
    def log_risultati(cls) :
        if cls.lista_risultati :
            for l in cls.lista_risultati :
                print(l)
                
        else :
            print("Lista risultati vuota")
            return
        
    #lista value
    @classmethod
    def log_valori_inseriti(cls) :
        if cls.lista_risultati :
            for l in cls.lista_valori_inseriti :
                print(l)
                
        else :
            print("Lista valori inseriti e vuota")
            return
    #metodo potenza
        @classmethod
    def potenza(cls, valori) : 
        result = valori[0]
        for valori in range(2,len(valori)) :
            result = result**valori
            cls.lista_valori_inseriti.append(valori)
        print (result)
        return cls.lista_risultati.append(result)
            
    
    
    
    
