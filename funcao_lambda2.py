#!/usr/bin/python3

# anonimas = [lambda x: x**2,
#             lambda x: x**3,
#             lambda x: x**4]
# for c in anonimas:
#     print(c(5)) #c vai ser inserido em x, Então 10**2


lamb = lambda a,b,c: ((b ** 2)-(4 * a * c))
print(lamb(3,-2,-5))
