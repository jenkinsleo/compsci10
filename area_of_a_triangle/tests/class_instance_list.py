import random

class Test():
    def __init__(self):
        self.classrandom = random.randint(0,10000000)

if __name__ == "__main__":

    l = []
    for x in range(1, 10):
        l.append(Test())

    for w in l:
        print(w.classrandom)