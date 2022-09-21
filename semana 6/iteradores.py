from unicodedata import name


a = "Persona"
a.__iter__()

print(a.__iter__())

b = ["Pedro","Masculino","22652831-2"]
b.__iter__()

print(b.__iter__())

"""nameI = iter(["Pedro", "David", "Gascon", "Mendoza"])
print(next(nameI))
print(next(nameI))
print(next(nameI))
print(next(nameI))
print(next(nameI))""" 

nameIter = iter(["Pedro", "Ana", "Juan", "Stefhania"])
for i in nameIter:
    print(i)