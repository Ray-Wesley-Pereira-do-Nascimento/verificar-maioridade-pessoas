from datetime import date

quant = 7
hoje = date.today().year
maiores = 0
menores = 0
for i in range(quant):
    while True:
        print("=" * 40)
        nasc = int(input("Digite uma data de nascimento no formato dd/mm/aaaa: "))
        print("=" * 40)
        if nasc > hoje:
            print("=" * 40)
            print("Data de nascimento inválida, digite novamente!")
            print("=" * 40)
        else:
            break
    idade = hoje - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print("=" * 40)
print(f"{maiores} das {quant} pessoas já atingiram a maioridade.")
print(f"{menores} das {quant} pessoas não atingiram a maioridade.")
print("=" * 40)
