#português brasil cachaça açúcar
with open("arquivo.txt", 'w') as f:
    print("abrindo...")
    f.write("uma frase qualquer na primeira linha\n")   
    f.write("o \\n com uma barra quebra linha\n")   
    f.write("com duas a gente imprime a própria barra\n")   
    
    print(f.closed)    
print(f.closed)

#português brasil cachaça açúcar
with open("arquivo2.txt", 'w') as f:
        #formatação
    # '{ id : . precision type }'
    f.write('{:s}\n'.format("português brasil cachaça açúcar!")) #imprimindo strings
    f.write('{:d}\n'.format(1))  #imprimindo inteiros
    f.write('{:.2e}\n'.format(1.963865200092e-3)) #imprimindo floats
    f.write('{:.2f}\n'.format(1.963865200092e-3))
    f.write('{:.2e}\n'.format(1.963865200092e4))
    f.write('{:.2f}\n'.format(1.963865200092e4))
    #imprimindo dois items simultaneamente
    f.write(" primeiro {:s} depois {:s}\n".format("os primeiros","os últimos"))
    f.write(" primeiro {1:s} depois {0:s}\n".format("os primeiros","os últimos"))

FMTsci = '{:.2e}\n' #científica
FMTdec = '{:.2e}\n' #decimal
print(FMTsci.format(6.02e23))
print(FMTdec.format(3.1415))
