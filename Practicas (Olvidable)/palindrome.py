def print_hi(name):
    cadena=input("inserta valor: ")
    numlet=len(cadena)-1
    inversed=""
    for seq in range(numlet, -1, -1):
#        print(seq)
        inversed=inversed + cadena[seq]
    print(inversed is cadena)
    if cadena is inversed:
        print("es palindrome")
    else:
        print("no es palindrome")
# press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
