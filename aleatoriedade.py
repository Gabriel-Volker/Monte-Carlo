import random
from statistics import mean
a = [0, 1]
media = []
for t in range(0,100):
    num_zero = 0
    num_um = 0
    tentativas = 0
    resultado = False
    dic = []
    while True:
        for c in range(0, 8):
            b = random.choice(a)
            if b == 0:
                num_zero = num_zero + 1
            elif b == 1:
                num_um = num_um + 1
            dic.append(b)
        tentativas = tentativas + 1
        print("tentativas ", tentativas)
        if dic == [1, 1, 1, 1, 0, 0, 0, 0]:
            print("tentativas ", tentativas)
            #print("numero de zeros", num_zero)
            #print("numero de um", num_um)
            media.append(tentativas)
            dic = []
            break
        dic = []
        num_um = int()
        num_zero = int()
print(mean(media))