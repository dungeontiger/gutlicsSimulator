import random, re
""" Perform all kinds of dice rols """
class Dice:

  """ Roll dice and return the total """
  def roll(self, numberOfDice, sides, modifier):
    sum = 0
    for _ in range(1, numberOfDice + 1):
      sum = sum + random.randint(1, sides)
    return sum + modifier

  """Short cut to roll a d20 """
  def d20(self):
    return self.roll(1,20,0)

  """Roll d20 with advantage, roll two and return the highest """
  def d20Advantage(self):
    roll1 = self.roll(1,20,0)
    roll2 = self.roll(1,20,0)
    if roll1 > roll2:
      return roll1
    return roll2

  """Roll d20 with disadvantage, roll two and return the lowest """
  def d20Disadvantage(self):
    roll1 = self.roll(1,20,0)
    roll2 = self.roll(1,20,0)
    if roll1 < roll2:
      return roll1
    return roll2

  """ split a string into the correct integer parts and return the roll e.g. 3d6+2 """
  def rollString(self, roll):
    # first remove spaces from string to make regex easy
    # TODO: Throw exception for bad string?
    s = roll.replace(' ', '')
    m = re.match(r"(\d*)[dD](\d*)(.*)", s).groups()
    dice = int(m[0])
    sides = int(m[1])
    mod = 0
    if (m[2] != ''):
      mod = int(m[2])
    return self.roll(dice, sides, mod)
    