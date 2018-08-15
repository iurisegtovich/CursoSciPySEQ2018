Palavra='livro'
palavra='colher'
print(id(Palavra))
print(repr(Palavra))
print(type(Palavra))
Frase='O '+Palavra+' está em cima da mesa.'
print(id(Frase))
print(repr(Frase))
FraseIgual='O livro está em cima da mesa.'
print(id(FraseIgual))
print(FraseIgual is Frase)
print(FraseIgual == Frase)
mesmaFrase=Frase
print(id(mesmaFrase))
print(mesmaFrase is Frase)
print(FraseIgual == Frase)

#pegar um nome previamente definido e vincular a um novo objeto
Frase='Não há colher alguma.'
print(id(Frase))
