p = 19 # large prime
g = 3 # generator

#private keys
a = 2
b = 5


# key generated
x = g**a % p
y = g**b % p

# shared keys
shareda = y**a %p # to a
sharedb = x**b %p # to b

# shareda == sharedb


