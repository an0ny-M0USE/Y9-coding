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

# Convert dictionary keys to a list we can remove from
keys_left = list(data.keys())

while keys_left:
    key = random.choice(keys_left)  # pick a random key
    print(f"{key}: {data[key]}")
    keys_left.remove(key)           # remove so it won't be chosen again
