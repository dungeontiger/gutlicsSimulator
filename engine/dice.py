import random
""" Perform all kinds of dice rols """
class Dice:

  """ Roll dice and return the total """
  def roll(self, numberOfDice, sides, modifier):
    sum = 0
    for _ in range(1, numberOfDice + 1):
      sum = sum + random.randint(1, sides)
    return sum + modifier
