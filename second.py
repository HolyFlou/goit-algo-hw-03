from random import sample

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or max-min < quantity: # Перевірка на обмеження
        return []
    ticket = sample(range(min, max), quantity)
    ticket.sort()
    return ticket 

print("Ваші лотерейні числа:", get_numbers_ticket(1000, 1200, 3))