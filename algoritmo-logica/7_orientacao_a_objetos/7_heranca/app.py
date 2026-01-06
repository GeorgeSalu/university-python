class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print("vrummmmm")

class Carro(Veiculo):
    def __init__(self, rodas, marca,teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar

ferrari = Carro(4, "ferrari", True)
print(ferrari.marca)

ferrari.ligar()

print(ferrari.teto_solar)

