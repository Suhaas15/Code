def AND(a,b):
    return a&b

def OR(a,b):
    return a|b

def XOR(a,b):
    return a^b

def NOT(a):
    return ~a

bits=0
n=10

#count 1 digits in the binary notation
# while(n>0):
#     bits+=AND(n,1)
#     n>>=1

# print(bits)

#
# mask=0
# i=0
# while i<=16:
#     mask|=(1<<i)
#     print(bin(mask))
#     i+=2

#get ith bit
# i=2
# while(i>0):
#     n>>=i
#     i-=0
# bits+=AND(n,1)
# print(bits)

#set ith bit
# i=1
# bits=1<<i
# print(OR(n,bits))

#set ith bit zero
i=1
bits=1<<i
NOT(bits)
print(AND(n,bits))
