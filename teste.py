palavra=input("Digite uma palavra")
nova_p =""

for x in range(0, len(palavra)):
    print(palavra[x], "\n", end="")

for x in palavra:
    nova_p = x + "*"
    print(nova_p, end="")


input()
 
