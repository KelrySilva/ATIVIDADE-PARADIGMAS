class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

    def mostrar(self):
        print(f"{self.nome} | {self.cargo} | Salario: R$ {self.salario:.2f} | Bonus: R$ {self.calcular_bonus():.2f}")


class FolhaPagamento:
    def __init__(self, limite):
        self.limite = limite
        self.lista = []

    def adicionar(self, funcionario):
        self.lista.append(funcionario)

    def processar(self):
        total = 0.0
        elegíveis = []

        for f in self.lista:
            if f.salario > self.limite:
                elegíveis.append(f)

        for f in elegíveis:
            f.mostrar()
            total += f.calcular_bonus()

        print(f"\nTotal gasto com bonus: R$ {total:.2f}")
        print(f"Funcionarios que recebem bonus: {len(elegíveis)}")


folha = FolhaPagamento(limite=3000.00)

folha.adicionar(Funcionario("Ana Silva",    "Engenheira de Software", 8500.00))
folha.adicionar(Funcionario("Bruno Costa",  "Analista Junior",        2800.00))
folha.adicionar(Funcionario("Carla Mendes", "Gerente de Produto",    11200.00))
folha.adicionar(Funcionario("Daniel Rocha", "Designer UX",            4300.00))
folha.adicionar(Funcionario("Eduarda Lima", "Estagiaria",             1500.00))
folha.adicionar(Funcionario("Fabio Souza",  "DevOps Engineer",        7000.00))

folha.processar()
