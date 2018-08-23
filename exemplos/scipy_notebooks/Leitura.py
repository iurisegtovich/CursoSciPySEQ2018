'''
esse módulo faz a leitura'''

def fazer_leitura():
    with open("input.txt", 'r') as f:
        varname=f.readline()
#        print("alimentando", varname, "em x")
        x=[]
        linha=f.readline()
        lista=linha.split(",")
        for xi in lista:
#            print("convertendo", xi)
            x.append(float(xi))
#    print("x: ",x)
    n=len(x)
#    print("n: ",n)
    with open("data.txt", 'r') as f:
        import csv
        data = csv.reader(f)
        next(data) # skip header
        T=[]
        P=[]
        for row in data:
            T.append(float(row[0]))
            P.append(float(row[1]))
#    print("T: ", T)
#    print("P: ", P)
    return n, x, T, P