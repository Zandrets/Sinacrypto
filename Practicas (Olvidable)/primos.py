def print_hi(name):
    num_prim=[]
    for seq in range(1 , 1000):
        if len(num_prim) == 0:
            num_prim.append(seq)
            continue
        if len(num_prim) == 1:
            num_prim.append(seq)
            continue
        for primos in num_prim:
            res=seq%primos
            if res == 0 and primos!=1:
                break
            last_num=len(num_prim)-1
            if primos == num_prim[last_num] and res != 0:
                num_prim.append(seq)
                break
    print(num_prim)
# press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
