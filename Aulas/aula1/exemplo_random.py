from random import random, seed

print("Com Random:")
for i in range(5):
    print(random())

print("\nCom a seed(20):")
seed(20)

for i in range(5):
    print(random())