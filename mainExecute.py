from CreateLabNodes import CreateLabNodesClass

CreateLabNodesClassInstance = CreateLabNodesClass()

for method in CreateLabNodesClassInstance.__dict__.values():
    try:
        print(method())
    except TypeError:
        pass
