def gcd(a,b):
    if a == 0:
        return b
    else :
        return gcd(b%a,b)

q = 19 # large prime no

a = 3 # private of alice & gcd(q,a) = 1
while gcd(a,q) != 1:
    a += 1

g = 2 # generator form cyclic group

# publishs g^a,g,q

b = 5 # bob private key
while gcd(b,q) != 1:
    b += 1
h = g**a**b

cyhper = "1012" * h
print(cyhper)
decypt = cyhper/ h
print(decypt)