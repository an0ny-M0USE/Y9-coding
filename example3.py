import time
def type_writer(text, delay=0.02):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(delay/100)
    print()

type_writer("hello this is coding", 2)