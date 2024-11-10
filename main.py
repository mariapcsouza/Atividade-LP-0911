from enum import Enum

class Loja: # Classe principal

    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.loja_mais_proxima = None
        self.funcionarios = [] # Permite agregação com a classe Funcionário
        self.estoque = [] # Faz composição com a classe Instrumento

    def __str__(self): # Permite impressao da loja mais perto
        if self.loja_mais_proxima:
            loja_proxima = self.loja_mais_proxima.localizacao
        else: 
            loja_proxima = "Não identificada"
        return f"Loja localizada em {self.localizacao}, mais próxima da filial {loja_proxima}"

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        funcionario.loja_atual = self # Muda o atributo loja_atual do funcionário para a instância atual 
    
    def demitir_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            funcionario.loja_atual = None # Funcionário perde relação com loja
    
    def adicionar_instrumento(self, instrumento):
        self.estoque.append(instrumento)

    def remover_instrumento(self, instrumento):
        if instrumento in self.estoque:
            self.estoque.remove(instrumento)

    def contar_instrumentos(self):
        instrumentos_por_tipo = {'Guitarra': 0, 'Baixo': 0, 'Violão': 0}
        for instrumento in self.estoque:
            if isinstance(instrumento, Guitarra):
                instrumentos_por_tipo['Guitarra'] += 1
            elif isinstance(instrumento, Baixo):
                instrumentos_por_tipo['Baixo'] += 1
            elif isinstance(instrumento, Violao):
                instrumentos_por_tipo['Violão'] += 1
        return instrumentos_por_tipo

    def contar_funcionários(self):
        funcionarios_por_cargo = {'GERENTE': 0, 'TECNICO': 0, 'VENDEDOR':0, 'ESTAGIARIO':0}
        for funcionario in self.funcionarios:
            if funcionario.cargo == Cargo.GERENTE:
                funcionarios_por_cargo['GERENTE'] +=1
            elif funcionario.cargo == Cargo.TECNICO:
                funcionarios_por_cargo['TECNICO'] += 1
            elif funcionario.cargo == Cargo.VENDEDOR:
                funcionarios_por_cargo['VENDEDOR'] += 1
            elif funcionario.cargo == Cargo.ESTAGIARIO:
                funcionarios_por_cargo['ESTAGIARIO'] += 1
        return funcionarios_por_cargo


class Cargo(Enum): # Cria hierarquia dos cargos
    GERENTE = 1
    TECNICO = 2
    VENDEDOR = 3
    ESTAGIARIO = 4

class Funcionario:

    def __init__(self, nome, cpf, salario, cargo):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        if isinstance(cargo, Cargo):
            self.cargo = cargo
        else:
            raise ValueError("Cargo inválido")
        self.loja_atual = None

class Instrumento:

    def __init__(self, marca, modelo, preco, numero_de_cordas):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.numero_de_cordas = numero_de_cordas

class Guitarra(Instrumento):

    def __init__(self, marca, modelo, preço, numero_de_cordas, tipo_ponte):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.tipo_ponte = tipo_ponte
               
class Baixo(Instrumento):

    def __init__(self, marca, modelo, preço, numero_de_cordas, passivo):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.passivo = passivo

class Violao(Instrumento):

    def __init__(self, marca, modelo, preço, numero_de_cordas, tipo_madeira):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.tipo_madeira = tipo_madeira

# Driver Code

loja1 = Loja("Botafogo")
loja2 = Loja("Flamengo")

print(loja1)

loja1.loja_mais_proxima = loja2
loja2.loja_mais_proxima = loja1

print(loja2)

funcionario1 = Funcionario("Peixonauta", "888.888.888-88", 50000, Cargo.GERENTE)
funcionario2 = Funcionario("Alexandre de Moraes", "012.345.678-90", 420, Cargo.ESTAGIARIO)

loja1.contratar_funcionario(funcionario1)
print(loja1.contar_funcionários())

guitarra1 = Guitarra("Tagima", "T-640", "2560", 6, "Tremolo")
baixo1 = Baixo("Strinberg", "PSB40", "1330", 4, True)
violao1 = Violao("Giannini", "GF-1D CEQ", "820", 6, "Sapele")

loja1.adicionar_instrumento(guitarra1)
loja1.adicionar_instrumento(baixo1)
loja1.adicionar_instrumento(violao1)

print(loja1.contar_instrumentos())

loja1.remover_instrumento(violao1)

print(loja1.contar_instrumentos())

loja1.demitir_funcionario(funcionario1)
loja1.demitir_funcionario(funcionario2)

print(loja1.contar_funcionários())