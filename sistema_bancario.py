class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            print("Não é possível depositar um valor negativo.")
    
    def saque(self, valor):
        if valor > 0 and valor <= 500:
            if valor <= self.saldo:
                self.saldo -= valor
                print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser positivo e no máximo R$ 500.")
    
    def extrato(self):
        print("Saldo atual: R$ {:.2f}".format(self.saldo))
    
    def exibir_menu(self):
        print("=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("0. Sair")

# Função principal
def main():
    conta = ContaBancaria()
    while True:
        conta.exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            valor = float(input("Digite o valor a depositar: "))
            conta.deposito(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a sacar: "))
            conta.saque(valor)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
