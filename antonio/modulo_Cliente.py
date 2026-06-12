class Cliente:
    
    n_clienti = 0
    
    def __init__(self, nome_cognome, email, password):
        self.nome_cognome = nome_cognome
        self.email = email
        self.password = password
        self.id_cliente = Cliente.conta_clienti() + 1 #in questo modo ho un intero incrementale, grazie al metodo statico che prima mi conta i clienti e poi assegna un +1 a tale valore
        self.wallet = 0 #il credito è zero inizialmente, è da prevedere un metodo per ricaricare il saldo
    
    @classmethod
    def conta_clienti(cls):
        return cls.n_clienti