# Uso da lib "random" para randomizar a senha
import random

# Variaveis de caracteres na senha

Maiu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Minu = "abcdefghijklmnopqrstuvwxyz"
Nume = "0123456789"
Simb = "!@#$%&*-+,."

Senha = Maiu + Minu + Nume + Simb

# Pergunta e funcionamento do código
while True:

    Tamanho = int(input("Qual o tamanho da senha que deseja criar ? > "))

    if Tamanho < 8 or Tamanho > 32:

        print("Senha muito pequena ou muito grande, por favor entre com uma senha entre 8 a 32 caracteres")
        
    else:

        criacao_Senha = ''.join(random.sample(Senha,Tamanho))
        print("Senha criada:", criacao_Senha) 

        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(criacao_Senha + '\n')

    break