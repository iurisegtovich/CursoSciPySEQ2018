a=1.
b=2.
c=3.

R=8.314

def v(n,T,P):
    return n*R*T/P
    
Tamb=298.15
Patm=1e5
def v_amb_atm(n):
    return v(n,T=Tamb,P=Patm)
    
print( v_amb_atm(3.) )
    
    


