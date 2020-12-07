import random

for i in range(1, 10):
    exact = random.randint(1, 6)
    offset = [0, 0, 5]
    level = random.randint(0, 2)
    dice = (exact + offset[level])
    if dice > 6:
        print(6)
    else:
        print(dice)


       
