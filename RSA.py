import sympy 
import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 

msg = input("Enter Your message :")
len1 = len(msg)
list1 = []
p = sympy.randprime(1000000000,9999999999)
q = p
while(p==q):
     q = sympy.randprime(1000000000,9999999999)

print("P is : ",p)
print("q is : ",q)

n = p*q
phi = (p-1)*(q-1)
print("n is : ",n)
print("phi is : ",phi)

for i in range(random.randrange(1,phi,1),phi):
  e=i
  if(gcd(e,phi)==1):
    break

print("e is : ",e)

d = modinv(e,phi)
     
print("d is : ",d)

for i in range(0,len1):
    a = ord(msg[i])
    list1.append(a)
print(list1)

cipher = []

for i in range(len1):
  x = pow(list1[i],e,n)
  cipher.append(x)

for x in cipher:
  print(x,end="  ")
print("")
plaintext = []

for i in range(len1):
  y = pow(cipher[i],d,n)
  plaintext.append(y)

print(plaintext)
fstr = ''
for i in range(len1):
  b = chr(plaintext[i])
  fstr+=b

print(fstr)
