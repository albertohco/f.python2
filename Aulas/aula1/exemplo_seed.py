import random

# Usando uma seed específica
print("Com seed(42):")
random.seed(42)
for i in range(3):
    print(random.random())

print("\nCom a mesma seed(42):")
random.seed(42)
for i in range(3):
    print(random.random())

print("\nCom seed diferente (123):")
random.seed(123)
for i in range(3):
    print(random.random())