#recursive function that receives a list and returns its sum value
def soma(lista):
    if (len(lista) == 1):
        return lista.pop()
    else:
        lastListValue = lista.pop()
        return lastListValue + soma(lista)

#recursive function that receives a list and returns its length
def countItens(lista):
    if(len(lista) == 1):
        lista.pop()
        return 1
    else:
        lista.pop()
        return 1 + countItens(lista)
            


#example of use
vectornum = [1,2,4,6]
vectornum2 = [1,2,4,6,1,2,3,4,6]
valorsoma = soma(vectornum)
numerodeItens = countItens(vectornum2)
print(valorsoma)
print(numerodeItens)