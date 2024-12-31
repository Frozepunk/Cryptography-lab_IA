import math 
p=int(input("Enter the value of p"))
q=int(input("Enter the value of q"))
n=p*q
phi_n=((p-1)*(q-1))
e=int(input("Enter the value of e"))
while e<phi_n:
    if math.gcd(e,phi_n)==1:
        e+=1
    d=pow(e,-1,phi_n)
m=int(input("Enter the value of M"))
c=math.pow(m,e)%n
de=math.pow(c,d)%n
print(c)
print(de)