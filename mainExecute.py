import CreateLabNodes

for callable in CreateLabNodes.__dict__.values():
    try:
        print(callable())
    except TypeError:
        pass
