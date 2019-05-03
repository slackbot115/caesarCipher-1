'''
Este e o nosso software de Cifra de Cesar em Python, criado por Lucas Anjos (https://github.com/luskas8) e Vinicius Carvalho (https://github.com/slackbot115).

A cifra de Cesar consiste em ser uma criptografia de substituicao, propriamente dito substitui letras de uma palavra por outras em função de dificultar a leitura humana.

Para utilizar a cifra e necessario:
    - A frase que voce deseja cifrar
    - A chave que seria basicamente um numero de 1 a 26, que seria o tanto de "casas" que seriam puladas ou passadas para se obter a nova frase

Exemplo: 

Frase sem encriptacao: criptografia
Chave: 13
A frase encriptada: pevcgbtensvn
'''

#Este metodo e utilizado para encriptar a palavra ou frase digitada
def cifrador(cifra, key):
    cifra.lower()
    new_char = ''

    for char in cifra:
        if char == ' ':
            new_char += ' '
        else:
            if ord(char)+key > 122:
                char = chr(((ord(char) + key) - 122) + 96)
            else:
                char = chr(ord(char) + key)

            new_char += char

    return new_char

#Este metodo e utilizado para decriptar a palavra ou frase digitada com a cifra de Cesar utilizando a forma de forca bruta (brute force)
def decriptar(cifra):
    cifra.lower()
    new_char = ''
    key = 1
    lista = []

    while True:
        for char in cifra:
            if char == ' ':
                new_char += ' '
            else:
                if ord(char) - key < 97:
                    char = chr(((ord(char) - key) - 97) + 123)
                else:
                    char = chr(ord(char) - key)
        
            new_char += char
        new_char += '\n'
        lista.append(new_char)
        new_char = ''
        if key >= 26:
            break
        else:
            key += 1

    wordlist = open("wordlistPortugues.txt", "r")
    listWord = wordlist.readlines()
    for word in lista:
        if word in listWord:
            return word
    else:
            return 'Palavra não semelhante a nada no portugues'
            exit()        

#Este metodo e utilizado para decriptar a palavra ou frase digitada com a cifra de Cesar ja conhecendo a chave de encriptacao
def decriptar_key(cifra, key):
    cifra.lower()
    new_char = ''
    
    for char in cifra:
        if char == ' ':
            new_char += ' '
        else:
            if ord(char) - key < 97:
                char = chr(((ord(char) - key) - 97) + 123)
            else:
                char = chr(ord(char) - key)
        
        new_char += char

    return new_char

#Inicia o programa dando as opcoes para a utilizacao do programa
def main():
    try:
        op = int(input('Digite a opção desejada: \n1 - Encriptacao \n2 - Decriptacao\n'))
        if op == 1:
            palavra = input('Digite o texto para ser cifrado: ')
            key = int(input('Digite a chave: '))
            print('Sua palavra cifrada ficou:',cifrador(palavra,key))
        elif op == 2:
            op = int(input('Deseja utilizar qual metodo\n 1 - brute force \n 2 - sabendo a chave \n'))
            if op == 1:
                palavra = input('Digite o texto para ser decriptado: ')
                print(decriptar(palavra))
            elif op == 2:
                palavra = input('Digite o texto para ser decriptado: ')
                key = int(input('Digite a chave: '))
                print(decriptar_key(palavra, key))
        else:
            print('Opcao digitada não existente, saindo do programa...')
            exit()
    except Exception as error:
        print('Ocorreu um erro:', error)

main()
