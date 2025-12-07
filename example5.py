import random

data = {
    1: "Line one",
    2: "Line two",
    3: "Line three",
    4: "Line four",
    5: "Line five",
    6: "Line six",
    7: "Line seven",
    8: "Line eight",
    9: "Line nine",
    10: "Line ten"
}

keys_left = list(data.keys())

for i in range(5):  # loop 5 times
    if not keys_left:
        break  # safety check

    key = random.choice(keys_left)
    print(f"{key}: {data[key]}")
    keys_left.remove(key)  # remove so it won't repeat
