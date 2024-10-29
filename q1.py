"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule 
a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.   

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua 
preferência ou pode ser previamente definido no código; 
"""

def check_if_number_is_in_fibonacci_seq(number: int):
    fibonacci_seq = [0, 1]
    while number > fibonacci_seq[-1]:
        fibonacci_seq.append(fibonacci_seq[-1]+fibonacci_seq[-2])
    if number in fibonacci_seq:
        print(f"O número {number} pertence a sequência de Fibonacci")
    else:
        print(f"O número {number} não pertence a sequência de Fibonacci")

if __name__=="__main__":
    number = int(input("Digite o número que deseja verificar: "))
    check_if_number_is_in_fibonacci_seq(number)