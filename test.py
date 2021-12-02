import random
tablica = []

for i in range(100):
    x = random.sample(range (1, 55), 5)
    tablica.append(x)
    

for i in tablica:
    print (i)
