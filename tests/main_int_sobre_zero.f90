program test

real x
integer i

read(*,*) x

print*, 123321/x

i=int(x)
print*, i

end program

! a divisão de inteiro por zero dá runtime error
!a conversão de infinity para inteiro da zero
