from math import log, exp
##rango=[1,2]
rango=[0,1]
#preformula=(4-(rango[0] ** 2)-(rango[0] ** 3))
#formula=(4-(rango[1] ** 2)-(rango[1] ** 3))
##preformula=(log(rango[0])+(rango[0] ** 2) -4)
##formula=(log(rango[1])+(rango[1] ** 2) -4)
preformula=(exp(rango[0]-1)-(3*rango[0]/2))
formula=(exp(rango[1]-1)-(3*rango[1]/2))
error=float(100)
print("F(",rango[0],") = ",preformula,", F(",rango[1],") =", formula)
print()
if (formula * preformula) < 0:
    while error > 1:
        print("F(",rango[0],") = ",preformula,", F(",rango[1],") =", formula)
        print("rango es de: ",rango)
        x=((rango[0]*formula)-(rango[1]*preformula))/(formula-preformula)
        print("el valor de X es: ", x)
        formula=(exp(x-1)-(3*x/2))
        if (formula * preformula) < 0:
            rango[1]=x
        if (formula * preformula) > 0:
            rango[0]=x
#        formula=(4-(rango[1] ** 2)-(rango[1] ** 3))
#        preformula=(4-(rango[0] ** 2)-(rango[0] ** 3))
##        preformula=(log(rango[0])+(rango[0] ** 2) -4)
##        formula=(log(rango[1])+(rango[1] ** 2) -4)
        preformula=(exp(rango[0]-1)-(3*rango[0]/2))
        formula=(exp(rango[1]-1)-(3*rango[1]/2))
        x2=((rango[0]*formula)-(rango[1]*preformula))/(formula-preformula)
        error=abs(((x2-x)/x2)*100)
        print("error es de: ", error)


    print("F(",rango[0],") = ",preformula,", F(",rango[1],") =", formula)
    print("rango es de: ",rango)
    x=((rango[0]*formula)-(rango[1]*preformula))/(formula-preformula)
    print("el valor de X es: ", x)
    formula=(exp(x-1)-(3*x/2))
    if (formula * preformula) < 0:
        rango[1]=x
    if (formula * preformula) > 0:
        rango[0]=x
##    preformula=(log(rango[0])+(rango[0] ** 2) -4)
##    formula=(log(rango[1])+(rango[1] ** 2) -4)
    preformula=(exp(rango[0]-1)-(3*rango[0]/2))
    formula=(exp(rango[1]-1)-(3*rango[1]/2))
    print("F(",rango[0],") = ",preformula,", F(",rango[1],") =", formula)
    print("rango es de: ",rango)