nota=50
custo=20 #café

troco=nota-custo
print("o seu troco é ",troco)

nota = troco
print("sobrou",nota)

custo=10 #bala
troco=nota-custo
print("o seu troco é ",troco)

nota = troco
print("sobrou",nota)

#################################

def compra(nota,custo):
    print('comprando', custo,'com',nota)
    troco=nota-custo
    print("sobrou",troco)    
    return troco
    
nota=compra(nota,5)
nota=compra(nota,15)
