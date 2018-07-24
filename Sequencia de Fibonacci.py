velho = 0
velho1 = 1
novo = 0
d = int(input("Digite quantos termos quer saber: "))
cont = 1
print("0",end=" ")
while cont != d:
    novo = velho + velho1
    print("{}".format(novo),end=' ')
    velho1 = velho
    velho = novo
    cont += 1

