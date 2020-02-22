import math 

ep = [4,1,2,3,2,3,4,1]
ip = [2,6,3,1,4,8,5,7]
p10 = [3,5,2,7,4,10,1,9,8,6]
p8 = [6,3,7,4,8,5,10,9]
p4 = [2,4,3,1]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

#function for XOR operaation
def XOR (a, b): 
    if a != b: 
        return 1
    else: 
        return 0

# calculate round 
def round(text,keyed):

      def DecimalToBinary(num): 
        if num > 1: 
            DecimalToBinary(num // 2) 
        temp_s0.append(num % 2)
      
      ip1 = []
      ip2 = []
      for i in range(4):
        ip1.append(text[i])
 
      for i in range(4,8):
        ip2.append(text[i])
  
      y = []
      for i in range(0,8):
        y.append(ip2[ep[i]-1]) 
     
      z = []
      for i in range(8):
        check = XOR(y[i],keyed[i])
        z.append(check)
  
      a0 = []
      a1 = []
      for i in range(4):
        a0.append(z[i])
      for i in range(4,8):
        a1.append(z[i])
     
      p = [a0[0],a0[3]]
      q = [a0[1],a0[2]]
      r = [a1[0],a1[3]]
      s = [a1[1],a1[2]]

      l=0
      n=0
      temp = 0
      for i in range(1,-1,-1):
        l = l + p[i]*math.pow(2,temp)
        n = n + r[i]*math.pow(2,temp)
        temp = temp + 1 

      l = (int(l))
      n = int(n)
      
      m = 0
      o = 0
      temp = 0
      for i in range(1,-1,-1):
        m = m + q[i]*math.pow(2,temp)
        o = o + s[i]*math.pow(2,temp)
        temp = temp + 1

      m = (int(m))
      o = int(o)
      
      t1 = S0[l][m]
      t2 = S1[n][o]
      temp_s0 = []
      s0 = []
      s1 = []
      
      if (t1==0 and t2==0):
        temp_s0=[0,0,0,0]
      elif(t1==1 and t2==0):
        temp_s0=[0,1,0,0]
      elif(t1==0 and t2==1):
        temp_s0=[0,0,0,1]
      elif(t1==1 or t2==1):
        if(t1==1):
          temp_s0.append(0)
          DecimalToBinary(t1)
          DecimalToBinary(t2)
        if(t2==1):
          DecimalToBinary(t1)
          temp_s0.append(0)
          DecimalToBinary(t2)
      elif (t1==0 and t2!=0):
        temp_s0.append(0)
        DecimalToBinary(t1)
        DecimalToBinary(t2)
      elif (t1!=0 and t2==0):
        DecimalToBinary(t1)
        DecimalToBinary(t2)
        temp_s0.append(0)
      else:
          DecimalToBinary(t1)
          DecimalToBinary(t2)

      after_p4 = []
      for i in range(4):
        after_p4.append(temp_s0[p4[i]-1])
      
      slot1 = []
      for i in range(4):
        slot1.append(XOR(after_p4[i],ip1[i]))

      final = slot1 + ip2
      return(final)


K = list(input("Enter 10 bit key Value : "))
size_of_key = len(K);
if(size_of_key != 10):
  K = list(input("Re-enter only 10 bit key value : "))

p1 = list(input("Enter 8 bit plaintetxt Value : "))
size_of_p = len(p1);
if(size_of_p != 8):
  p1 = list(input("Re-enter only 8 bit plaintext : "))

key = []
for i in range(10):
  key.append(int(K[i])) 

plaintext = []
for i in range(8):
  plaintext.append(int(p1[i])) 

print("")
print("Generated Keys are :")

#for p10 operation
key1 = []
for i in range(0,10):
  key1.append(key[p10[i]-1]) 

#for first left shift
LS_1_1 = [0,0,0,0,0]

for i in range(0,5):
  if(i==4):
    LS_1_1[i] = key1[0]
  else:
    LS_1_1[i] = key1[i+1]


LS_1_2 = [0,0,0,0,0]
a=0
for i in range(5,10):
  if(i==9):
    LS_1_2[a] = key1[5]
    a=a+1
  else:
    LS_1_2[a] = key1[i+1]
    a=a+1

#converting into p8
LS_1 = LS_1_1 + LS_1_2
K1 = []
for i in range(8):
  K1.append(LS_1[p8[i]-1])

print("K1 is : ",K1)

#for second left shift
LS_2_1 = LS_1_1.copy()
LS_2_2 = LS_1_2.copy()

for i in range(0,5):
  if(i>=3):
    LS_2_1[i] = LS_1_1[i-3]

  else:
    LS_2_1[i] = LS_1_1[i+2]

for i in range(0,5):
  if(i>=3):
    LS_2_2[i] = LS_1_2[i-3]

  else:
    LS_2_2[i] = LS_1_2[i+2]

LS_2 = LS_2_1 + LS_2_2
K2 = []

#second time convert into p8
for i in range(8):
  K2.append(LS_2[p8[i]-1])

print("K2 is : ",K2)

# for round 1
x = []
for i in range(0,8):
    x.append(plaintext[ip[i]-1]) 

returned_from_round1 = round(x,K1)

# for round 2
swap1 = []
swap2 = []
for i in range(8):
  if i < 4 : 
    swap2.append(returned_from_round1[i])
  else:
    swap1.append(returned_from_round1[i])

final_swap = (swap1+swap2)
returned_from_round2 = round(final_swap,K2)
ciphertext = [0,0,0,0,0,0,0,0]
for i in range(8):
    a = ip[i]-1
    ciphertext[a] = returned_from_round2[i]
print("")
print("After Encryption :")
print("ciphertext :",ciphertext)
print("")
#for Decryption
#This is for round 3
A = []
for i in range(0,8):
    A.append(ciphertext[ip[i]-1])

first_round_of_decryption = round(A,K2)

# for round 4
swap1_2 = []
swap2_2 = []
for i in range(8):
  if i < 4 : 
    swap2_2.append(first_round_of_decryption[i])
  else:
    swap1_2.append(first_round_of_decryption[i])

final_swap_2 = (swap1_2 + swap2_2)
second_round_of_decryption = round(final_swap_2,K1)
plainttext_2 = [0,0,0,0,0,0,0,0]
for i in range(8):
    a = ip[i]-1
    plainttext_2[a] = second_round_of_decryption[i]

print("After Decryption")
print("plaintext : ",plainttext_2)
