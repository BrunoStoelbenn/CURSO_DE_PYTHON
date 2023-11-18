import sys
# Generator expression, Iterables e Iterators em Python
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))
# print()
# for item in iterator:
#     print(item)



# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)

i = 0
while i <= 1000:
    print(next(generator))
    i += 1

