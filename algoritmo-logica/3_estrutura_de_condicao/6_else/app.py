poupanca = 200
saque = 300

if saque <= poupanca:
    print("voce sacou R$%d reais"%saque)
else:
    print("voce nao tem saldo para sacar R$%d"%saque)
    print("sua poupanca tem no momento R$%d"%poupanca)