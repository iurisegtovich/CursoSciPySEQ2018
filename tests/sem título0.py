with open("arquivo.txt", 'w') as f:
    
    print("abrindo...")
    f.write("uma frase qualquer na primeira linha")   
    f.write("\n")
    
    #formatação
    # '{ id : . precision type }'
    f.write('{:s}\n'.format("olá")) #imprimindo strings
       
    f.write('{:d}\n'.format(1))  #imprimindo inteiros
    
    f.write('{:.2e}\n'.format(1.963865200092e-3)) #imprimindo decimais
    f.write('{:.2f}\n'.format(1.963865200092e-3))
    f.write('{:.2e}\n'.format(1.963865200092e4))
    f.write('{:.2f}\n'.format(1.963865200092e4))
    
    #imprimindo várias coisas
    f.write("{:.2f} is greater than {:.2f}\n".format(2.,1.5))

