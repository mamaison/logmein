import random

def shuffle_cards(items):
    max = len(items)
    for i in range(max -1):
        number = random.randint(1, max)
        item = items[i]
        items[i] = items[number]
        items[number] = item
        max -=1
