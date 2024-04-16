import os

def adicionar_lembrete(lembrete):
    with open("lembretes.txt", "a") as arquivo:
        arquivo.write(lembrete + "\n")

def listar_lembretes():
    if os.path.exists("lembretes.txt"):
        with open("lembretes.txt", "r") as arquivo:
            lembretes = arquivo.readlines()
            if lembretes:
                print("Lembretes:")
                for i, lembrete in enumerate(lembretes, 1):
                    print(f"{i}. {lembrete.strip()}")
            else:
                print("Não há lembretes.")
    else:
        print("Não há lembretes.")

def apagar_lembrete(numero):
    if os.path.exists("lembretes.txt"):
        with open("lembretes.txt", "r") as arquivo:
            lembretes = arquivo.readlines()
        with open("lembretes.txt", "w") as arquivo:
            for i, lembrete in enumerate(lembretes, 1):
                if i != numero:
                    arquivo.write(lembrete)
        print("Lembrete apagado com sucesso.")
    else:
        print("Não há lembretes.")

def main():
    while True:
        print("\n1. Adicionar lembrete")
        print("2. Listar lembretes")
        print("3. Apagar lembrete")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            lembrete = input("Digite o lembrete: ")
            adicionar_lembrete(lembrete)
        elif escolha == "2":
            listar_lembretes()
        elif escolha == "3":
            listar_lembretes()
            numero = int(input("Digite o número do lembrete que deseja apagar: "))
            apagar_lembrete(numero)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
