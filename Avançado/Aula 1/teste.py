class MinhaClasse:

    def __init__(self, nome, sobrenome):
        self.umNome = nome
        self.umsobrenome = sobrenome
    
    def mostra_nome(self):
        print(self.umNome, self.umsobrenome)

obj1 = MinhaClasse('Raoni', 'Silva')
obj2 = MinhaClasse('Dani', 'Amorim')
obj3 = MinhaClasse('Naiara', 'Santina')

obj1.mostra_nome()
obj2.mostra_nome()

obj2.umNome = 'Maya'
obj2.mostra_nome()
obj3.mostra_nome()