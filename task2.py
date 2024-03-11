from random import randint
from typing import List

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
  if not (1 <= min <= max <= 1000):
    return []

  if not (1 <= quantity <= max - min + 1):
    return []

  numbers_set = set()
  while len(numbers_set) < quantity:
    numbers_set.add(randint(min, max))

  return sorted(list(numbers_set))
try:
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
except ValueError as e:
    print("Error:", e)