import rabdom
from random import randint

def get_numbers_tiket(min, max, qantity):
    list_number = []

    if min < 1 or max > 1000:
        return list_number
    
    while len(list_number) != qantity:
        x = randint(min, max)
        if x not in list_number:
            list_number.append(x)
    list_number = list_number.sorted()
    return list_number

if __name__ == "__main__":
    
    min = int(input())
    max = int(input())
    qantity = int(input())
    get_numbers_tiket()

