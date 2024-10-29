"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja 
maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.   

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código;
"""

if __name__=="__main__":
    times_occured = 0
    user_input = input("Digite a string a ser verificada: ")
    for char in user_input:
        if char.lower() == 'a':
            times_occured += 1

    if times_occured == 0:
        print("Não há ocorrências da letra 'a' na frase informada")
    else:
        print(f"A letra 'a' ocorre {times_occured} vezes na frase informada")