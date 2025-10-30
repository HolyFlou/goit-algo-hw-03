from random import randint

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min < quantity > max: # Перевірка на обмеження
        return []
    nums = []
    randomnum = randint(min, max)
    nums.append(randomnum)
    for i in range(quantity-1):
        randomnum = randint(min, max)
        for num in nums: # Перевірка на унікальність чисел
            if randomnum == num:
                while randomnum == num:
                    randomnum = randint(min, max)
        nums.append(randomnum)
    nums.sort() # Сортування списку
    return nums

print("Ваші лотерейні числа:", get_numbers_ticket(-10, 10, 5))