import random

cargo = ["ink", "ink", "ink", "thread", "thread",
         "paper", "paper", "paper", "paper", "glue"]

removed = cargo.pop(random.randint(0,len(cargo)))
print(removed)
print(*cargo, sep=", ")

