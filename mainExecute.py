import CreateLabNodes

instclass = CreateLabNodes.CreateLabNodesClass()

'''
print(instclass.login())
print(instclass.createLab())
print(instclass.createRouter1())
print(instclass.createRouter2())
print(instclass.createRouter3())
print(instclass)
print(instclass)
print(instclass)
print(instclass.)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
print(instclass)
'''
method_list = [func for func in dir(instclass) if callable(getattr(instclass, func))]

print(method_list)

for method in method_list:
    try:
        method()
    except TypeError:

        pass
