from decimal import Decimal as dec
from decimal import localcontext

from decimal import getcontext

print(getcontext())
x=dec(1)/dec(7)
print(x)
y=x+x+x+x+x+x+x
print(y)


with localcontext() as ctx:
    print(ctx)
    ctx.prec=50
    x=dec(1)/dec(7)
    print(x)
    y=x+x+x+x+x+x+x
    print(y)

