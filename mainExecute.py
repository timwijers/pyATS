import CreateLabNodes

for callable in CreateLabNodes.CreateLabNodesClass.__dict__.values():
    try:
        print(callable())
    except TypeError:
        pass

# instclass = CreateLabNodes.CreateLabNodesClass()

# print(instclass.login())
